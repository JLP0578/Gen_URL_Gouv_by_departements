import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

class DepartementURL:
    def __init__(self, departement, domaine, ERNT):
        self.nom = departement["nom"]
        self.code = departement["code"]
        self.domaine = domaine["URL"]
        self.domaineVerif = domaine["verified"]
        self.ERNT = ERNT["URL"]
        self.ERNTVerif = ERNT["verified"]
       
    def outObjet(self):
        return {
            "nom": self.nom,
            "code": self.code,
            "URLs": {
                "domaine": {
                    "URL": self.domaine,
                    "verified": self.domaineVerif
                },
                "E.RNT": {
                    "URL": self.ERNT,
                    "verified": self.ERNTVerif
                }
            }
        }