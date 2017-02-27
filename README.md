# BookmarksPy

Busca uma url randomicamente nos favoritos do firefox, e abre no navegador padrao. 
Search for a random url in firefox favorites, and open in the default browser.

Change the absolute path of the places.sqlite database (Temporary solution):
db = sqlite3.connect("/home/myuser/.mozilla/firefox/my_folder.default/places.sqlite")

Example 1, list all folders containing links:

    $ python random_bookmarks_firefox.py -l
    ID
    2   Menu de favoritos
    3   Barra de favoritos
    5   Outros favoritos
    7   Ubuntu and Free Software links
    12   Mozilla Firefox

    Try using: $ python random_bookmarks_firefox.py -i 12
    

Example 2, show links and open a url of ID 7 (7  Ubuntu and Free Software links): 

    $ python random_bookmarks_firefox.py -i 7

    Pasta pesquisada : Ubuntu and Free Software links

    http://www.ubuntu.com/
    http://wiki.ubuntu.com/
    https://answers.launchpad.net/ubuntu/+addquestion
    http://www.debian.org/


Example 3, Searches for folders containing:

    $ python random_bookmarks_firefox.py -p Ubuntu

    Busca as pastas que contenham :  Ubuntu

    Pasta(s) pesquisada(s) :
    Ubuntu and Free Software links

    http://www.ubuntu.com/
    http://wiki.ubuntu.com/
    https://answers.launchpad.net/ubuntu/+addquestion
    http://www.debian.org/



Esse é meu primeiro script no github, estou aprendendo a usar essa ferramenta.
This is my first github script, I'm learning to use this tool.

contato: juan.carvalho82@gmail.com
