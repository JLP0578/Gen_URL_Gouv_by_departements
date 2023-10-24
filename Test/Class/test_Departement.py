import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.Departement import Departement

def test_Departement():
    NOM = "Ain"
    CODE = "01"
    OUTPUT = {"nom": NOM,"code": CODE}
    OBJECT = Departement(NOM, CODE)

    assert OBJECT.nom == NOM
    assert OBJECT.code == CODE
    assert Departement.outObjet(OBJECT) == OUTPUT
