import calculatrice
while 1:
    i=input("donner un mot et tapez Q pour quiter  ")
    if i=='Q':
        l=input("vous etes sur de vouloir quitter le programme?,non pour continuer  ")
        if l=='non':
            print( "Vous allez continuez")
            continue
        else:
            print( "Vous avez choisis de quittez")
            break
    print(" le mot que vous avez tapez est ",i)


