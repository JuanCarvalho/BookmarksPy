# BookmarksPy

> Redescubra seus favoritos! Abra URLs aleatórias dos seus favoritos do Firefox diretamente no terminal.

## 📖 Sobre

BookmarksPy é um utilitário de linha de comando em Python que permite explorar seus favoritos do Firefox de forma aleatória. Perfeito para quando você quer redescobrir sites antigos ou simplesmente deixar a sorte escolher sua próxima leitura!

## ✨ Funcionalidades

- 📋 **Listar todas as pastas** de favoritos
- 🔍 **Buscar pastas** por nome ou termo
- 🎲 **Abrir URL aleatória** de uma pasta específica
- 🎰 **Abrir URL aleatória** de todos os favoritos
- 🚀 **Auto-detecção** do banco de dados do Firefox

## 📋 Pré-requisitos

- Python 2.7+
- Firefox instalado com favoritos salvos
- Sistema operacional: Linux/Unix (testado em Ubuntu)

> **Nota:** Todas as dependências (sqlite3, argparse, webbrowser) fazem parte da biblioteca padrão do Python.

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/JuanCarvalho/BookmarksPy.git
cd BookmarksPy
```

2. Torne o script executável (opcional):
```bash
chmod +x random_bookmarks_firefox.py
```

## 💻 Uso

### Listar todas as pastas de favoritos

```bash
python random_bookmarks_firefox.py -l
```

**Saída de exemplo:**
```
ID    Nome da Pasta
2     Menu de favoritos
3     Barra de favoritos
5     Outros favoritos
7     Ubuntu and Free Software links
12    Mozilla Firefox
```

### Abrir URL aleatória de uma pasta específica (por ID)

```bash
python random_bookmarks_firefox.py -i 7
```

**Saída de exemplo:**
```
Pasta pesquisada: Ubuntu and Free Software links

http://www.ubuntu.com/
http://wiki.ubuntu.com/
https://answers.launchpad.net/ubuntu/+addquestion
http://www.debian.org/

Abrindo URL aleatória...
```

### Buscar pastas por nome e abrir URL aleatória

```bash
python random_bookmarks_firefox.py -s Ubuntu
```

**Saída de exemplo:**
```
Busca as pastas que contenham: Ubuntu

Pasta(s) pesquisada(s):
Ubuntu and Free Software links

http://www.ubuntu.com/
http://wiki.ubuntu.com/
https://answers.launchpad.net/ubuntu/+addquestion
http://www.debian.org/

Abrindo URL aleatória...
```

### Abrir URL aleatória de TODOS os favoritos

```bash
python random_bookmarks_firefox.py -a
```

## 🔧 Opções disponíveis

| Opção | Forma longa | Descrição |
|-------|-------------|-----------|
| `-l` | `--listar` | Lista todas as pastas de favoritos com seus IDs |
| `-i ID` | `--id ID` | Abre URL aleatória da pasta com o ID especificado |
| `-s TERMO` | `--search TERMO` | Busca pastas que contenham o termo e abre URL aleatória |
| `-a` | `--all` | Abre URL aleatória de todos os favoritos |

## 🔍 Como funciona

1. **Detecção automática:** O script localiza automaticamente o banco de dados SQLite do Firefox (`~/.mozilla/firefox/*.default/places.sqlite`)
2. **Consulta SQL:** Extrai os favoritos consultando as tabelas `moz_bookmarks` e `moz_places`
3. **Filtragem:** Filtra URLs baseado nos parâmetros fornecidos
4. **Seleção aleatória:** Escolhe uma URL aleatória do conjunto filtrado
5. **Abertura:** Abre a URL no navegador padrão do sistema

## 📝 Exemplos práticos

### Redescobrir conteúdo de tecnologia
```bash
# Buscar e abrir site aleatório de pastas relacionadas a Python
python random_bookmarks_firefox.py -s Python
```

### Exploração aleatória
```bash
# Deixe a sorte decidir! Abre qualquer favorito
python random_bookmarks_firefox.py -a
```

### Workflow típico
```bash
# 1. Ver todas as pastas disponíveis
python random_bookmarks_firefox.py -l

# 2. Escolher uma pasta interessante (ex: ID 12)
python random_bookmarks_firefox.py -i 12
```

## 📄 Licença

Este projeto está licenciado sob a GPL - veja o cabeçalho do arquivo para detalhes.

## 👤 Autor

**Carlos Alberto Batista Carvalho**
- Email: juan.carvalho82@gmail.com
- GitHub: [@JuanCarvalho](https://github.com/JuanCarvalho)

## 🤝 Contribuindo

Contribuições, issues e feature requests são bem-vindos!

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📊 Status do Projeto

Versão: **1.0.1**
Status: **Em manutenção**

---

⭐ Se este projeto foi útil para você, considere dar uma estrela!
