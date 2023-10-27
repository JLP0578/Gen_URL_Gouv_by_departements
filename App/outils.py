from unidecode import unidecode
import requests
import json
import time
import re

def isValidPage(statusCode):
    return statusCode == 200

def isResetPage(statusCode):
    return statusCode == 101

def isOnlyChar(string):
    return bool(re.match(r'^[A-Za-z]+$', string))

def isOnlyInt(string):
    return bool(re.match(r'^[0-9]+$', string))

def addOnceInTab(tab, element):
    if element not in tab:
        tab.append(element)
    return tab

def remove_accents(input_str):
    return unidecode(input_str)

def remove_apostroph(nom_lower):
    return nom_lower.replace("'", "") 

def json_write(PathBuild, jsonContent):
    with open(PathBuild+".json", 'w', encoding='utf-8') as f:
        json.dump(jsonContent, f, ensure_ascii=False, indent=4)

def json_load(PathBuild):
    with open(PathBuild+".json", 'r', encoding='utf-8') as f:
        return json.load(f)

def autoCreateDomaine(departementNom):
    nom_lower = departementNom.lower()
    nom_replace = remove_apostroph(nom_lower)
    nom = remove_accents(nom_replace)
    return "https://www."+nom+".gouv.fr/"
    
def autoCreateERNT_1(domaine):
    domaine = domaine.lower()
    return domaine+"Actions-de-l-Etat/Risques-naturels-et-technologiques"

def autoCreateERNT_2(domaine):
    domaine = domaine.lower()
    return domaine+"Actions-de-l-Etat/Environnement-risques-naturels-et-technologiques"

def autoCreateERNT_3(domaine):
    domaine = domaine.lower()
    return domaine+"Actions-de-l-Etat/Environnement/Risques"

def autoCreateERNT_4(domaine):
    domaine = domaine.lower()
    return domaine+"Actions-de-l-Etat/Environnement.-risques-naturels-et-technologiques"

def isValidURL(URL):
    regex_pattern  = r'((?<=[^a-zA-Z0-9])(?:https?\:\/\/|[a-zA-Z0-9]{1,}\.{1}|\b)(?:\w{1,}\.{1}){1,5}(?:com|org|edu|gov|uk|net|ca|de|jp|fr|au|us|ru|ch|it|nl|se|no|es|mil|iq|io|ac|ly|sm){1}(?:\/[a-zA-Z0-9]{1,})*)'
    matches = re.finditer(regex_pattern, URL)
    for match in matches:
        return True
    
    return False

def executeRequest(URL):
    print("TEST URL :", URL)
    return {"code": 404, "return": False}
# REPENSE CE CODE
    time.sleep(60)
    if isValidURL(URL):
        headers = {
            'User-Agent': 'Gecko/20100101'
        }
        response = requests.get(URL, headers=headers)
        print(response)
        if isValidPage(response.status_code):
            return {"code": response.status_code, "return": True}
        else: 
            if isResetPage(response.status_code):
                return {"code": response.status_code, "return": True}
            else:
                return {"code": 404, "return": False}
    else:
        return {"code": 404, "return": False}

        