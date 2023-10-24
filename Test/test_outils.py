import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App import outils
import ENV

def test_outils_Bool():
    VALID_STATUS_CODE = [{"int":200,"bool": True},{"int":400,"bool": False},{"int":"200","bool": False},{"int":"ezez","bool": False}]
    for ints in VALID_STATUS_CODE:
        assert outils.isValidPage(ints["int"]) == ints["bool"]

    TEST_STRINGS = [{"string":"Bonjour","bool": True},{"string":"bonjour","bool":True},{"string":"Bon5jour", "bool": False},{"string":"bon5jour", "bool": False},{"string":"Bonjour3", "bool": False},{"string":"bonjour3", "bool": False},{"string":"3Bonjour", "bool": False},{"string":"3bonjour", "bool": False}]
    for strings in TEST_STRINGS:
        assert outils.isOnlyChar(strings['string']) == strings['bool']

    TEST_INTS = [{"int":"123", "bool": True}, {"int":"a123", "bool": False}, {"int":"123a", "bool": False}, {"int":"12a3", "bool": False}, {"int":"123.56", "bool": False}, {"int":"12f3", "bool": False}]
    for int in TEST_INTS:
        assert outils.isOnlyInt(int["int"]) == int["bool"]

def test_outils_tab():
    TAB = [1, 2, 3, 4]
    ELEMENT = 3
    assert outils.addOnceInTab(TAB, ELEMENT) == TAB

def test_jsonWrite():
    jsonContent = {"key1": "value1", "key2": "value2"}
    file_path = ENV.PATH_BUILD+r'\test\test'
    outils.json_write(file_path, jsonContent)
    assert outils.json_load(file_path) == jsonContent