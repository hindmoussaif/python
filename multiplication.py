def multiplication():
    a=input("donner le nmb à multiplier ")
    m=input("donner le chiffre de commencemant ")
    x=input("donner le chiffre de fin ")
    a=int(a)
    m=int(m)
    x=int(x)
    i=0
    k=0
    for i in range (m,x):
        k=a*i
        print(a," * ",i," = ",k)
        i+=1
r=input("bonjour, pour multiplication tappez multi pour le carré tappez car ")
if r=='multi':
    multiplication()
elif r=='car':
    x=input("donner ne nbr voulu ")
    x=int(x)
    car=lambda x: x*x
    print( "le carré de ",x,"= ",car(x))
else:
    print ("au revoir! ")