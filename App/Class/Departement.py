import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App import outils

class Departement:
    def __init__(self, nom, code):
        self.nom = nom
        self.code = code
       
    def outObjet(self):
        return {
            "nom": self.nom,
            "code": self.code
        }