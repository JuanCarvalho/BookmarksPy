#!/usr/bin/env python
# coding=utf-8

__author__ = "Carlos Alberto Batista Carvalho"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Carlos A. B. Carvalho"
__email__ = "juan.carvalho82@gmail.com"
__status__ = "Test"
__python__ = "2.7"

"""
    Busca uma url randomicamente nos favoritos do firefox, e abre no navegador padrao. 
    Search for a random url in firefox favorites, and open in the default browser.
"""

import random
import sqlite3
import webbrowser
import argparse
import sys
import traceback
import os

def find_database_places():
	"""
		Finding the database where firefox stores bookmarks
	"""
	# get home path user
	home = os.environ['HOME']
	# get home folder firefox
	dir_firefox = os.path.join(home, '.mozilla/firefox')
	# get folder *.default, where are sqlite database
	dir_default = [name_dir for name_dir in os.listdir(dir_firefox) if name_dir.endswith('.default')][0]
	# absolute place database
	database = os.path.join(dir_firefox, dir_default, 'places.sqlite')
	return database



# Init connection with sqlite
db = sqlite3.connect(find_database_places())

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--listar", help="Lista as pastas dos favoritos", action="store_true")
parser.add_argument("-p", "--pasta", help="Busca por pastas que contenham o termo", action="store_true")
parser.add_argument("-s", "--search", help="Busca links que contenham o termo", action="store_true")
parser.add_argument("-i","--id", help="Busca pelo id da pasta", action="store_true")
parser.add_argument("-a","--all", help="Busca uma pagina aleatória em todas as pastas", action="store_true")
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
    ultimo_id_mostrado = ''
    pastas = db.execute("select * from moz_bookmarks where type=2").fetchall()
    print 
    print "ID"
    for i in pastas:
        if i[5].encode('utf-8').lower() == 'tags':
            id_tags = i[0]
        if i[3] != id_tags:
            # Não printar itens da lista de pastas que não retornam url's
            if not i[5].encode('utf-8') in lista_ignorados:
                # Save the last id to show in the example below
                ultimo_id_mostrado = i[0]
                print i[0], " ", i[5].encode('utf-8')
    print
    print "Try using: $ python random_bookmarks_firefox.py -i {0}".format(ultimo_id_mostrado)
    print

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

if args.search:
    # Buscar links que contenham a palavra recebida como argumento
    # Find links containing the word received as an argument
    print "Under development"
    print "Find links containing the word received as an argument"