import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.DepartementURL import DepartementURL

def test_DepartementURL():
    DEPARTEMENT = {"nom": "Ain","code": "01"}
    DOMAINE_OBJ = {"URL": "https://xxx.xx/", "verified": False}
    ERNT_OBJ = {"URL": "https://xxx.xx/xxx/xxx", "verified": False}
    OUTPUT = {
        "nom": "Ain",
        "code": "01", 
        "URLs": {
            "domaine": DOMAINE_OBJ,
            "E.RNT": ERNT_OBJ
        }
    }


    OBJECT = DepartementURL(DEPARTEMENT, DOMAINE_OBJ, ERNT_OBJ)
    # test output
    assert DepartementURL.outObjet(OBJECT) == OUTPUT
    # test propriete 
    assert OBJECT.nom == DEPARTEMENT["nom"]
    assert OBJECT.code == DEPARTEMENT["code"]
    assert OBJECT.domaine == DOMAINE_OBJ["URL"]
    assert OBJECT.domaineVerif == DOMAINE_OBJ["verified"]
    assert OBJECT.ERNT == ERNT_OBJ["URL"]
    assert OBJECT.ERNTVerif == ERNT_OBJ["verified"]