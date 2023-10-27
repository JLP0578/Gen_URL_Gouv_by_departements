import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

import requests
from bs4 import BeautifulSoup

from App.Class.Departement import Departement
from App import outils

class ScrapWiki:
    def __init__(self):
        self.URLWiki = "https://fr.wikipedia.org/wiki/D%C3%A9partement_fran%C3%A7ais"
        self.DepartementScraped = []

    def makeRequest(self):
        response = requests.get(self.URLWiki)
        if outils.isValidPage(response.status_code):
            self.getDIV(response)
            return response
        else:
            print("La requête HTTP a échoué. Code de statut :", response.status_code)

    def getDIV(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        parent_div = soup.find('div', {'class': 'colonnes'})
        if parent_div:
            self.getUL(parent_div)
            return parent_div
        else:
            print("La div parente avec la classe spécifique n'a pas été trouvée sur la page.")
            
    def getUL(self, parent_div):
        ul_list = parent_div.find_all('ul')
        if ul_list:
            for ul in ul_list:
                self.getLIs(ul)
            return ul_list
        else:
            print("La liste <ul> n'a pas été trouvée à l'intérieur de la div parente.")

    def getLIs(self, ul):
        li_elements = ul.find_all('li')
        if li_elements:
            for li in li_elements:
                tab = self.DepartementScraped
                element = self.getNomAndCode(li)
                self.DepartementScraped = outils.addOnceInTab(tab, element)
            return li_elements
        else:
            print("La balise <li> n'a pas été trouvée à l'intérieur de la ul parente.")

    def getNomAndCode(self, li):
        code_element = li.find('code')
        a_element = li.find_all('a')
        a_element = a_element[-1]
        if code_element and a_element:
            a_text = a_element.get_text()
            code_text = code_element.get_text()
            dep = Departement(a_text, code_text)
            return Departement.outObjet(dep)

    def outObjet(self):
        output = []
        for departement in self.DepartementScraped:
            nom = departement['nom']
            code = departement['code']
            output.append(Departement.outObjet(Departement(nom, code)))
        return output

