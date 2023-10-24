class Departement:
    def __init__(self, nom, code):
        self.nom = nom
        self.code = code

    def outObjet(self):
        return {
            "nom": self.nom,
            "code": self.code
        }







# # Création d'une instance de la classe
# objet = NomDepartement("Valeur1", "Valeur2")

# # Utilisation des attributs de l'objet
# print(objet.attribut1)
# print(objet.attribut2)

# # Appel d'une méthode de l'objet
# objet.methode()