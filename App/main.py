import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.ScrapWiki import ScrapWiki
from App import outils
import ENV

def start():
    print("START")
    sw = ScrapWiki()

    print("MAKE REQUEST")
    ScrapWiki.makeRequest(sw)

    print("OUT")
    jsonContent = ScrapWiki.outObjet(sw)
    print(jsonContent)
    
    print("WRITE")
    file_path = ENV.PATH_BUILD+r"\wikiData"
    outils.json_write(file_path, jsonContent)

start()