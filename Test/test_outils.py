import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App import outils
import ENV

def test_outils_return():
    VALID_STATUS_CODE = [{"int":200,"return": True},{"int":400,"return": False},{"int":"200","return": False},{"int":"ezez","return": False}]
    for ints in VALID_STATUS_CODE:
        assert outils.isValidPage(ints["int"]) == ints["return"]

    RESET_STATUS_CODE = [{"int":101,"return": True},{"int":400,"return": False},{"int":"200","return": False},{"int":"ezez","return": False}]
    for ints in RESET_STATUS_CODE:
        assert outils.isResetPage(ints["int"]) == ints["return"]

    TEST_STRINGS = [{"string":"Bonjour","return": True},{"string":"bonjour","return":True},{"string":"Bon5jour", "return": False},{"string":"bon5jour", "return": False},{"string":"Bonjour3", "return": False},{"string":"bonjour3", "return": False},{"string":"3Bonjour", "return": False},{"string":"3bonjour", "return": False}]
    for strings in TEST_STRINGS:
        assert outils.isOnlyChar(strings['string']) == strings['return']

    TEST_INTS = [{"int":"123", "return": True}, {"int":"a123", "return": False}, {"int":"123a", "return": False}, {"int":"12a3", "return": False}, {"int":"123.56", "return": False}, {"int":"12f3", "return": False}]
    for int in TEST_INTS:
        assert outils.isOnlyInt(int["int"]) == int["return"]

    # TEST_URLS = [{"URL":"https://www.indre-et-loire.gouv.fr/", "return": True}, {"URL":"https://www.indre-et-loire.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques", "return": True}]
    # for URL in TEST_URLS:
    #     assert outils.executeRequest(URL["URL"]) == URL["return"]
    
    TEST_URLS = [{"URL":"https://www.indre-et-loire.gouv.fr/", "return": True}, {"URL":"https://www.indre-et-loire.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques", "return": True}, {"URL":"https://www.xxxx.gouv.fr/", "return": True}, {"URL":"https:.xxxx./", "return": False}]
    for URL in TEST_URLS:
        assert outils.isValidURL(URL["URL"]) == URL["return"]

def test_outils_remove_accents():
    text_with_accents = "Café au Lèvres: mélange spécialité"
    text_with_no_accents = "Cafe au Levres: melange specialite"
    assert outils.remove_accents(text_with_accents) == text_with_no_accents

def test_outils_remove_apostroph():
    text_with_apostroph = "l'arbre"
    text_with_no_apostroph = "larbre"
    assert outils.remove_apostroph(text_with_apostroph) == text_with_no_apostroph

def test_outils_tab():
    TAB = [1, 2, 3, 4]
    ELEMENT = 3
    assert outils.addOnceInTab(TAB, ELEMENT) == TAB

def test_jsonWrite():
    jsonContent = [{"nom": "Ain", "code": "01"}]
    file_path = ENV.PATH_BUILD_TEST
    outils.json_write(file_path, jsonContent)
    assert outils.json_load(file_path) == jsonContent

def test_autoCreate():
    TEST_NOMS = [{"nom":"Type", "return": "https://www.type.gouv.fr/"},{"nom":"typ45e", "return": "https://www.typ45e.gouv.fr/"}]
    for nom in TEST_NOMS:
        assert outils.autoCreateDomaine(nom["nom"]) == nom["return"]
    
    TEST_DOMAINES = [{"domaine":"https://www.type.gouv.fr/", "return": "https://www.type.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques"},{"domaine":"https://www.typ45e.gouv.fr/", "return": "https://www.typ45e.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques"}]
    for domaine in TEST_DOMAINES:
        assert outils.autoCreateERNT_1(domaine["domaine"]) == domaine["return"]
    
    TEST_DOMAINES = [{"domaine":"https://www.type.gouv.fr/", "return": "https://www.type.gouv.fr/Actions-de-l-Etat/Environnement-risques-naturels-et-technologiques"},{"domaine":"https://www.typ45e.gouv.fr/", "return": "https://www.typ45e.gouv.fr/Actions-de-l-Etat/Environnement-risques-naturels-et-technologiques"}]
    for domaine in TEST_DOMAINES:
        assert outils.autoCreateERNT_2(domaine["domaine"]) == domaine["return"]
    
    TEST_DOMAINES = [{"domaine":"https://www.type.gouv.fr/", "return": "https://www.type.gouv.fr/Actions-de-l-Etat/Environnement/Risques"},{"domaine":"https://www.typ45e.gouv.fr/", "return": "https://www.typ45e.gouv.fr/Actions-de-l-Etat/Environnement/Risques"}]
    for domaine in TEST_DOMAINES:
        assert outils.autoCreateERNT_3(domaine["domaine"]) == domaine["return"]

    TEST_DOMAINES = [{"domaine":"https://www.type.gouv.fr/", "return": "https://www.type.gouv.fr/Actions-de-l-Etat/Environnement.-risques-naturels-et-technologiques"},{"domaine":"https://www.typ45e.gouv.fr/", "return": "https://www.typ45e.gouv.fr/Actions-de-l-Etat/Environnement.-risques-naturels-et-technologiques"}]
    for domaine in TEST_DOMAINES:
        assert outils.autoCreateERNT_4(domaine["domaine"]) == domaine["return"]

