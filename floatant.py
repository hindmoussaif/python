def affiche_flottant(flotant):
    try:
        flotant=str(flotant) 
        pe,pf = flotant.split(".")
        return ",".join([pe,pf[0:3]])
    except ValueError:
        print("le numéro doit etre un flotant ")
reponse=str()
while reponse.lower() !='q':
    a=input("donner un floatant ")
    result=affiche_flottant(a)
    print(result)
    reponse=input("si vous voullez arreter cliquer sur Q , pour contunier n'importe ")
    

