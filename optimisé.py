y= input("choos a year de 4 chiffres ")
try:
    y=int(y)
    assert y<9999 and y>0
except ValueError as exception_retournee :
    print("l'année que vous avez rentré est incorrecte , l'erreur est : ", exception_retournee)
except AssertionError:
    print ("merci de choisir une année (positive) de 4 chiffre ")
else :
    if y % 4 == 0 and (y % 100 == 0  and y % 400 == 0) or (y % 100 != 0 )   :
        print('the year',y, 'is bissextil')
    else:
        print( "the year",y," is not bissextil")