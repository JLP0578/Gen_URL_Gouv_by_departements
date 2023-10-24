import os
import sys
from bs4 import BeautifulSoup

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.ScrapWiki import ScrapWiki
from App.Class.Departement import Departement

SHALLOW_LI = """<li><code>01</code> : <a>Ain</a></li>"""
SHALLOW_UL = """<ul>"""+SHALLOW_LI+"""</ul>"""
SHALLOW_DIV = """<div class="colonnes">"""+SHALLOW_UL+"""</div>"""
SHALLOW_PARENT = """<body>"""+SHALLOW_DIV+"""</body>"""
OUTPUT = {"nom": "Ain","code": "01"}
sw = ScrapWiki()
soup_li = BeautifulSoup(SHALLOW_LI, 'html.parser')
soup_ul = BeautifulSoup(SHALLOW_UL, 'html.parser')
soup_div = BeautifulSoup(SHALLOW_DIV, 'html.parser')
soup_parent = BeautifulSoup(SHALLOW_PARENT, 'html.parser')

DEPARTEMENT_1 = Departement.outObjet(Departement("Ain", "01"))
DEPARTEMENT_2 = Departement.outObjet(Departement("Aisne", "02"))

def extract_text_content(tag_list):
    return [str(tag.get_text()) for tag in tag_list]

def test_ScrapWiki_MakeRequest():
    assert extract_text_content(ScrapWiki.getUL(sw, soup_parent)) == extract_text_content(soup_div)
    assert extract_text_content(ScrapWiki.getUL(sw, soup_div)) == extract_text_content(soup_ul)
    assert extract_text_content(ScrapWiki.getLIs(sw, soup_ul)) == extract_text_content([soup_li])
    assert ScrapWiki.getNomAndCode(sw, soup_li) == OUTPUT

def test_ScrapWiki():
    assert ScrapWiki.outObjet(sw) == [DEPARTEMENT_1]
