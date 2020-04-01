
def calculatrice() :
    print("bonjour ")
    a=input("donner le premier chiffre ")
    a=int(a)
    b=input("donnée le 2éme chiffre  ")
    b=int(b)
    c=input("quel est l'operation que vous voullez effectuer + - *  /")
    c=str(c)
    result=int()
    if c=='+':
        result= a + b
    elif c=='-':
        result=a-b
    elif c=='*':
        result=a*b
    elif c=='/':
        if b==0:
            print("vouz ne pouvez pas déviser sur 0 ")  
        else:
            result=a/b
    return result
reponse='o'
totale=0
while reponse=='o':
    r=calculatrice()
    totale+=r
    print("le totale est : ",totale)
    reponse=input('vouler vous ajouter autre chose? o/n ')
    reponse=reponse.lower()