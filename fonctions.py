from random import choice
from try import *

def choisir_un_mot():
    return choice(liste_mot)
def recup_lettre():
    l=input("donner une lettre ")
    l=l.lower()
    return l
def recup_mot_masque(mot_complet, lettres_trouvees):   
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque