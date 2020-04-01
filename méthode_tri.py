#___________________ trier avec des clés précis _____________________________
# class Etudiant:
#     def __init__(self):
#         self.etudiants=[]
#     lambda colonnes : colonnes[x]
# #execution 
# etudiants=Etudiant()
# etudiants = [
#     ("Clément", 14, 16),
#     ("Charles", 12, 15),
#     ("Oriane", 14, 18),
#     ("Thomas", 11, 12),
#     ("Damien", 12, 15),
# ]
# #print(sorted(etudiants))""" python execute le sorted sur la 1ere colonne par défaut"""
# print(sorted(etudiants, key=lambda colonnes: colonnes[2]))
#___________________ tri d'une liste en utilisant lambda.attribut  _____________________________
class Etudiant:
    def __init__(self,prenom,age,note):
        self.prenom=prenom
        self.age=age
        self.note=note
    def __repr__(self):
        return "<Étudiant {} (âge={}, note={})> \n".format(
                self.prenom, self.age, self.note)
#liste etudiant par des instance de la classe Etudiant 
etudiants = [
    Etudiant("Clément", 14, 16),
    Etudiant("Charles", 12, 15),
    Etudiant("Oriane", 14, 18),
    Etudiant("Thomas", 11, 12),
    Etudiant("Damien", 12, 15),
]
"""sur le key lambda on met objet.attribut"""
#print(sorted(etudiants,key=lambda etudiants: etudiants.note , reverse=True))
"""pour trier sans utiliser lambda """
from operator import attrgetter
"""attrgetter accepte plusieurs critére de tri"""
print(sorted(etudiants, key=attrgetter("note","prenom",)))
# #liste etudiant par des tulpes 
# etudiants = [
#     ("Clément", 14, 16),
#     ("Charles", 12, 15),
#     ("Oriane", 14, 18),
#     ("Thomas", 11, 12),
#     ("Damien", 12, 15),
# ]
# """sur le key lambda on met objet[indice]"""
# #print(sorted(etudiants,key=lambda etudiants: etudiants[2] , reverse=True))
# """pour trier sans utiliser lambda """
# from operator import itemgetter
# print(sorted(etudiants, key=itemgetter(1)))