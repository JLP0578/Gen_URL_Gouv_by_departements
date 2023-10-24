import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

class DepartementURL:
    def __init__(self, departement, url):
        self.departement = departement
        self.url = url
       
    def outObjet(self):
        return {
            "nom": self.departement['nom'],
            "code": self.departement['code'],
            "URLs": {
                "domaine": self.url,
                "E.RNT": self.url
            }
        }