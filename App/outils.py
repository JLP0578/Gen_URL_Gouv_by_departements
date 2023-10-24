import re
import json

def isValidPage(statusCode):
    return statusCode == 200

def isOnlyChar(string):
    return bool(re.match(r'^[A-Za-z]+$', string))

def isOnlyInt(string):
    return bool(re.match(r'^[0-9]+$', string))

def addOnceInTab(tab, element):
    if element not in tab:
        tab.append(element)
    return tab

def json_write(PathBuild, jsonContent):
    with open(PathBuild+".json", 'w', encoding='utf-8') as f:
        json.dump(jsonContent, f, ensure_ascii=False, indent=4)

def json_load(PathBuild):
    with open(PathBuild+".json", 'r', encoding='utf-8') as f:
        return json.load(f)