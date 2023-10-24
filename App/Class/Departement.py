class Departement:
    def __init__(self, nom, code):
        self.nom = nom
        self.code = code

    def outObjet(self):
        return {
            "nom": self.nom,
            "code": self.code
        }