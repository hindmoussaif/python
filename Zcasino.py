import math
import random
import string 
solde=input("declarer ton solde ")
solde=int(solde)
reponse=str()
while solde>0 :
    try:
        mise=input ("hello winner , how much u play ")
        nbr=input("choose a number between 0 to 49  ")
        mise=int(mise)
        nbr=int(nbr)
        a= random.randrange(50)
        assert nbr >= 0 and nbr<50
        if a==nbr:
            solde=solde+(mise*3)
            print("Félicitation , Vous avez gangné ",mise*3)
        elif (a%2==0 and nbr%2==0) or (a%2 != 0 and nbr%2 != 0):
            solde = solde + math.ceil( mise * 0.5)
            print(" vous avez gagné ",mise * 0.5)
        else:
            print("Essayer une autre fois") 
        reponse=input("voulez vous continez? O/N ") 
        if reponse.lower() =="o":
             continue
        else:
            break 
    except AssertionError:
        print("le numéro doit etre entre 0 et 49 ")
    
         





