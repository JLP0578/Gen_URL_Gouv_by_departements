import os
import sys

current_dir = os.path.dirname(__file__) # Obtenez le chemin du répertoire actuel du script
parent_dir = os.path.dirname(current_dir) # Obtenez le chemin du répertoire parent
sys.path.append(parent_dir) # Ajoutez le répertoire parent à sys.path

from App.Class.Departement import Departement
from App.Class.DepartementURL import DepartementURL
from App import outils
import ENV

# renseigne code departmeent or select it in list
# gen domaine
# verif domaine
# gen ENRT
# verif ERNT
# 
# save


class AutoGenURL:
    def __init__(self, tabCodes):
        self.CodeSelected = tabCodes
        self.DepartementScraped = []

    def MakeGen(self, file_path):
        departementJson = outils.json_load(file_path)
        output = []
        for departement in departementJson:
            if departement["code"] in self.CodeSelected:
                dep_domaine = {"URL": "", "verified": False}
                dep_ernt = {"URL": "", "verified": False}
                domaine = self.genDomaine(departement['nom'])
                domaine_verif = outils.executeRequest(domaine)
                if outils.isValidPage(domaine_verif):
                    dep_domaine = {"URL": domaine, "verified": True}
                    
                    ernt = self.genErnt()
                    ernt_verif = outils.executeRequest(ernt)
                    if outils.isValidPage(ernt_verif):
                        dep_ernt = {"URL": ernt, "verified": True}

                    else:
                        dep_ernt = {"URL": ernt, "verified": False}
                        print("["+str(ernt_verif["code"])+"] Ernt: non vérifié")
                else:
                    dep_domaine = {"URL": domaine, "verified": False}
                    print("["+str(domaine_verif["code"])+"] Domaine: non vérifié")

                depURL = DepartementURL(departement, dep_domaine, dep_ernt)
                self.DepartementScraped = outils.addOnceInTab(output, DepartementURL.outObjet(depURL))
            else:
                print("skip")
                depURL = DepartementURL(departement, {"URL": "", "verified": False}, {"URL": "", "verified": False})
                self.DepartementScraped = outils.addOnceInTab(output, DepartementURL.outObjet(depURL))

        return output
            

    def genDomaine(self, nom):
        return outils.autoCreateDomaine(nom)

    def genErnt(self, domaine):
        ernt_1 = outils.autoCreateERNT_1(domaine)
        ernt_2 = outils.autoCreateERNT_2(domaine)
        ernt_3 = outils.autoCreateERNT_3(domaine)
        ernt_4 = outils.autoCreateERNT_4(domaine)
        verif_ernt = ""
        # OFF LINE
        # if outils.executeRequest(ernt_1):
        #     verif_ernt = ernt_1
        # elif outils.executeRequest(ernt_2):
        #     verif_ernt = ernt_2
        # elif outils.executeRequest(ernt_3):
        #     verif_ernt = ernt_3
        # elif outils.executeRequest(ernt_4):
        #     verif_ernt = ernt_4

        return verif_ernt

    def outObjet(self):
            return self.DepartementScraped

#     def MakeAutoGen(self, file_path):
#         departementJson = outils.json_load(file_path)
#         output = []
#         departementJson_len = len(departementJson)
#         actual_len = 0
#         for departement in departementJson:
#             actual_len = actual_len + 1
#             print(str(actual_len)+"/"+str(departementJson_len))
#             verif_domaine = ""
#             verif_ernt = ""
#             domaine = outils.autoCreateDomaine(departement['nom'])
#             web_verif = outils.executeRequest(domaine)
#             if web_verif["return"] and outils.isValidPage(web_verif["code"]):
#                 verif_domaine = domaine
#                 verif_ernt = ""
#                 # verif_ernt = self.choixERNT(domaine)
#                 depURL = DepartementURL(departement, verif_domaine, verif_ernt)
#                 self.DepartementScraped = outils.addOnceInTab(output, DepartementURL.outObjet(depURL))
#             if web_verif["return"] and outils.isResetPage(web_verif["code"]):
#                 print("REST CONNECTION ENABLE :(")
#                 break
#         return output
    
#     def choixERNT(self, domaine):
#         ernt = outils.autoCreateERNT_1(domaine)
#         if outils.executeRequest(ernt):
#             verif_ernt = ernt
#         else:
#             ernt = outils.autoCreateERNT_2(domaine)
#             if outils.executeRequest(ernt):
#                 verif_ernt = ernt
#             else:
#                 ernt = outils.autoCreateERNT_3(domaine)
#                 if outils.executeRequest(ernt):
#                     verif_ernt = ernt
#                 else:
#                     ernt = outils.autoCreateERNT_4(domaine)
#                     if outils.executeRequest(ernt):
#                         verif_ernt = ernt

#         return verif_ernt

#     def outObjet(self):
#         return self.DepartementScraped