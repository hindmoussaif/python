from random import choice
liste_mot=list()
liste_mot=['simulation','marriage','confinement','dejeuner','domistique']
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
reponse='o'
score=0
while reponse =='o':
    mot=choisir_un_mot()
    lettres_trouvees=list()
    mot_trouver=recup_mot_masque(mot,lettres_trouvees)
    niveau=input("Quel niveau vous voullez ? facile=f, moyen=m ou defficile=d ")
    niveau=niveau.lower()
    if niveau=='f':
        chance=len(mot)*2
    elif niveau=='m':
        chance=len(mot)*1.5
    elif niveau == 'd':
        chance=len(mot)+2
    else:
        chance=len(mot)*1.5
        print("le niveau par defaut est moyen ")
    print("le mot choisis se compose de ", len(mot)," lettres")

    while mot!= mot_trouver and chance>0:    
        l=input("donner une lettre  ")
        l=str(l)
        if l in mot_trouver:
            print('deja trouvée')
        elif l in mot:
            lettres_trouvees.append(l)
        mot_trouver=recup_mot_masque(mot,lettres_trouvees)
        print(mot_trouver)
        chance-=1 
    if mot_trouver==mot:  
        score+=chance 
        print("bravooooo ton score est " ,score)
    else:
        print("vous avez perdu !")
    
    reponse=input("est ce que vous voullez continuer? O/N ")
    reponse=reponse.lower()
 
