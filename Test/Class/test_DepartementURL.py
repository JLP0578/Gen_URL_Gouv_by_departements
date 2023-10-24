import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.DepartementURL import DepartementURL

def test_DepartementURL():
    DEPARTEMENT = {"nom": "Ain","code": "01"}
    URL = "https://xxx.xx/"
    OUTPUT = {"nom": "Ain","code": "01", "URLs": {"domaine": URL, "E.RNT": URL}}


    OBJECT = DepartementURL(DEPARTEMENT, URL)
    assert DepartementURL.outObjet(OBJECT) == OUTPUT