import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.AutoGenURL import AutoGenURL
from App.Class.ScrapWiki import ScrapWiki
from App import outils
import ENV

def START_SCRAP_WIKI():
    print("--- START_SCRAP_WIKI ---")
    print("- START")
    sw = ScrapWiki()

    print("- MAKE REQUEST")
    ScrapWiki.makeRequest(sw)

    print("- OUT")
    jsonContent = ScrapWiki.outObjet(sw)
    # print(jsonContent)
    
    print("- WRITE")
    outils.json_write(ENV.PATH_BUILD_WIKI, jsonContent)

def START_AUTO_GEN_URL():
    print("--- START_AUTO_GEN_URL ---")
    print("- START")
    tabCodes = ["04", "05", "06", "13", "84"]
    agu = AutoGenURL(tabCodes)

    print("- MAKE AUTO GEN")
    AutoGenURL.MakeGen(agu, ENV.PATH_BUILD_WIKI)

    print("- OUT")
    jsonContent = AutoGenURL.outObjet(agu)
    print(jsonContent)

    print("- WRITE")
    outils.json_write(ENV.PATH_BUILD_GEN, jsonContent)

START_SCRAP_WIKI()
START_AUTO_GEN_URL()
