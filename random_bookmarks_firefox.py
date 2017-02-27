#!/usr/bin/env python
# coding=utf-8

__author__ = "Carlos Alberto Batista Carvalho"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Carlos A. B. Carvalho"
__email__ = "juan.carvalho82@gmail.com"
__status__ = "Production"
__python__ = "2.7"

"""
    Busca uma url randomicamente nos favoritos do firefox, e abre no navegador padrao 
"""

import random
import sqlite3
import webbrowser
import argparse
import sys
import traceback

# Caminho para o arquivo places.sqlite
db = sqlite3.connect("/home/juan/.mozilla/firefox/odwanb5d.default/places.sqlite")

# O banco moz_places armazenam historico, favoritos e outras coisas...
# O nome do banco dos sites favoritos é moz_bookmarks
# As chaves estrangeiras (fk) do banco moz_bookmarks, são os id's do banco moz_places

# EXEMPLO DE COMO SÃO SALVOS OS DADOS NOS FAVORITOS (moz_bookmarks)
# id == Chave unica
# type == tipo de arquivo 1(link), 2(folder)
# fk == id no banco moz_places 
# parent == id no banco moz_bookmarks

# id|type|fk|parent|position|title|keyword_id|folder_type|dateAdded|lastModified|guid
# 24|2||2|4|Django|||1466105656533000|1466105658578000|CGrTi1bmEIsa
### o parent do favorito abaixo é o id da pasta onde ele esta localizado (parent 24 pertence à pasta com o id 24, "Django")	
# 35|1|20|24|3|Django: Image Files Uploading Example - 2015|||1466105656980000|1466105656980000|Er_Xu1_LagIa


parser = argparse.ArgumentParser()

parser.add_argument("-l", "--listar", help="Lista as pastas dos favoritos", action="store_true")
parser.add_argument("-p", "--pasta", help="Busca por pastas que contenham o termo", action="store_true")
parser.add_argument("-s", "--search", help="Busca links que contenham o termo", action="store_true")
parser.add_argument("-i","--id", help="Busca pelo id da pasta", action="store_true")
parser.add_argument("-a","--all", help="Busca uma pagina aleatória em todas as pastas", action="store_true")
# opcao nargs=? significa argumento opcional
parser.add_argument("Arg",help="Termo para busca", type=str, nargs='?',)

# Se não houver arg mostra o help
if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

if args.pasta:
	print
	print "Busca as pastas que contenham : ", args.Arg
	print
	lista_de_pastas = {}
	str_busca = args.Arg.lower()
	# Lista contendo os id's dos sites favoritos
	# chaves_estrangeiras = db.execute("select fk from moz_bookmarks").fetchall()
	chaves_estrangeiras = []
	pastas = db.execute("select * from moz_bookmarks where type=2").fetchall()
	print "Pasta(s) pesquisada(s) :"
	for i in pastas:
		try:
			# encode('utf-8') para evitar o erro
			# UnicodeEncodeError: 'ascii' codec can't encode character u'\xe3' in position 1: ...
			if str_busca in i[5].encode('utf-8').lower():
				print i[5].encode('utf-8')
				cmd = "select fk from moz_bookmarks where parent='%s'"%str(i[0])
				for i in db.execute(cmd).fetchall():
					chaves_estrangeiras.append(i[0])
		except: 
			traceback.format_exc()
	print
	lista_url = []
	for i in chaves_estrangeiras:
		# percorre a lista de id's e retorna a url 
		cmd = "select url from moz_places where id='%s'"%str(i)
		# Executa a consulta
                try:
        	    str_url = db.execute(cmd).fetchall()[0][0]
		    if str_url[:4] == "http":
			print str_url
			# se a string retornada iniciar com http adiciona à lista de url's
			lista_url.append(str_url)
                except:
                    pass

	new = 2 # open in a new tab, if possible
	# Busca uma url na lista_url, um indice randomico que seja 1 valor a menos que o tamanho da lista
	url = lista_url[random.randrange(len(lista_url))]
	# Abre o navegador padrão
	webbrowser.open(url,new=new)
	print

# Lista de pastas que não retornam srings
lista_ignorados = ["", "Tags", "Favoritos", "mobile"]
if args.listar:
	id_tags = ''
	pastas = db.execute("select * from moz_bookmarks where type=2").fetchall()
	print "ID"
	for i in pastas:
		if i[5].encode('utf-8').lower() == 'tags':
			id_tags = i[0]
		if i[3] != id_tags:
			# Não printar itens da lista de pastas que não retornam url's
			if not i[5].encode('utf-8') in lista_ignorados:
				print i[0], " ", i[5].encode('utf-8')

if args.id:
	lista_de_pastas = {}
	str_busca = args.Arg.lower()
	# Lista contendo os id's dos sites favoritos
	# chaves_estrangeiras = db.execute("select fk from moz_bookmarks").fetchall()
	chaves_estrangeiras = []
	cmd1 = "select * from moz_bookmarks where id=%s"%str_busca
	nome_pasta = db.execute(cmd1).fetchall()
	print
	print "Pasta pesquisada :", nome_pasta[0][5]

	try:
		cmd = "select fk from moz_bookmarks where parent=%s"%str_busca
		for i in db.execute(cmd).fetchall():
			chaves_estrangeiras.append(i[0])
	except: 
		traceback.format_exc()
	print
	lista_url = []
	for i in chaves_estrangeiras:
		try:
			# percorre a lista de id's e retorna a url 
			cmd = "select url from moz_places where id='%s'"%str(i)
			# Executa a consulta
			str_url = db.execute(cmd).fetchall()[0][0]
			if str_url[:4] == "http":
				print str_url
				# se a string retornada iniciar com http adiciona à lista de url's
				lista_url.append(str_url)
		except:
			traceback.format_exc()

	new = 2 # open in a new tab, if possible
	# Busca uma url na lista_url, um indice randomico que seja 1 valor a menos que o tamanho da lista
	url = lista_url[random.randrange(len(lista_url))]
	# Abre o navegador padrão
	webbrowser.open(url,new=new)
	print

if args.all:
	
	# Lista contendo os id's dos sites favoritos
	chaves_estrangeiras = db.execute("select fk from moz_bookmarks").fetchall()
	
	lista_url = []
	for i in chaves_estrangeiras:
		try:
			if i[0] != None:
				# percorre a lista de id's e retorna a url 
				cmd = "select url from moz_places where id='%s'"%str(i[0])
				# Executa a consulta
				str_url = db.execute(cmd).fetchall()[0][0]
				if str_url[:4] == "http":
					# se a string retornada iniciar com http adiciona à lista de url's
					lista_url.append(str_url)
		except:
			traceback.format_exc()



	new = 2 # open in a new tab, if possible
	# Busca uma url na lista_url, um indice randomico que seja 1 valor a menos que o tamanho da lista
	url = lista_url[random.randrange(len(lista_url) - 1)]
	# Abre o navegador padrão
	webbrowser.open(url,new=new)
