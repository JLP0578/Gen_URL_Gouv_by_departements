import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.AutoGenURL import AutoGenURL
from App import outils
import ENV

# def test_AutoGenURL():
#     agurl = AutoGenURL()
#     print(ENV.PATH_BUILD_TEST)
#     DEPARTEMENT = {
#         "nom": "Ain",
#         "code": "01"
#     }
#     OUTPUT = [{
#         "nom": "Ain",
#         "code": "01",
#         "URLs": {
#             "domaine": "https://www.ain.gouv.fr/",
#             "E.RNT": "https://www.ain.gouv.fr/Actions-de-l-Etat/Risques-naturels-et-technologiques"
#         }
#     }]
#     # OUTPUT = [{
#     #     "nom": "Ain",
#     #     "code": "01",
#     #     "URLs": {
#     #         "domaine": "https://www.ain.gouv.fr/",
#     #         "E.RNT": ""
#     #     }
#     # }]

#     departementJson = outils.json_load(ENV.PATH_BUILD_TEST)
#     print(departementJson)
#     assert AutoGenURL.MakeAutoGen(agurl, ENV.PATH_BUILD_TEST) == OUTPUT

def test_AutoGenURL():
    codeSelected = ["01"]
    agurl = AutoGenURL(codeSelected)
    assert agurl.CodeSelected == codeSelected

    OUTPUT = [{
        "nom": "Ain",
        "code": "01",
        "URLs": {
            "domaine": {
                "URL": "https://www.ain.gouv.fr/",
                "verified": False
            },
            "E.RNT": {
                "URL": "",
                "verified": False
            }
        }
    }]
    assert AutoGenURL.MakeGen(agurl, ENV.PATH_BUILD_TEST) == OUTPUT
    assert agurl.DepartementScraped == OUTPUT
    # save

