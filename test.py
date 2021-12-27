from math import *
# age=int(input("donnez votre age "))
# if age>=18:
#     print("majeur, vous l etes depuis ",age-18, " ans")
# else:
#     print("mineur","vous serez majeur dans ",18-age,"ans")

#r=int (input("donnez un chiffre "))

# if r>=4: 
#     if r<=8:
#         print("le chiffre",r ,"est correcte")
#     else :
#         print("ce chiffre n'est pas bon")
# else:
#     print("ce chiffre n'est pas bon")

# if r>=4 and r<=8:
#     print("oui")
# else:
#     print("non") 
# i=1
# while i<=r :
#     print(" 7 *",i,"=",7*i)
#     i=i+1

# r=int (input("donnez un chiffre entre 1 et 3 "))
# while r<1 or r>3 :
#     r=int (input("donnez un autre chiffre "))
# print (" bravo ")

# a=int(input("donnez a"))
# if a>0:
#     print("positif")
# elif a==0:
#     print("null")
# else:
#     print("negatif")
# a=int (input("donnez un chiffre entre 1 et 3 "))
# if a>=1 and a<=3:
#     print("bravo")
# else:
#     print("nul")
# i=1
# while(i<=10):
#     print(7*i)
#     i=i+1

# i=1
# r=0
# x=int(input("donnez un chiffre "))
# while i<=x :
#     r=r+i
#     i=i+1
# print("le résultat est : ",r)
# i=1
# r=1
# x=int(input("donnez un chiffre "))
# while i<=x :
#     r=r*i
#     i=i+1
# print("le résultat est : ",r)


# i = 1
# m = 0
# while i<=3 :
#     print("donnez le chifrre numéro", i )
#     nb=int(input(" "))
#     if  nb > m :
#         m = nb
#     i=i+1
# print("Le MIN est : ",m)

# i = 1
# print("donnez le chifrre numéro", i )
# nb=int(input(" "))
# m=nb
# while nb!=0 :
#     i=i+1
#     print("donnez le chifrre numéro", i )
#     nb=int(input(" "))
#     if  nb > m :
#         m = nb
# print("Le MAX est : ",m)


# i=0
# y=0
# n=int(input("donnez un nbr "))
# while i<=n :
#     y=y+i
#     i=i+1
# print("le resultat est :" ,y)

# y=0
# n=int(input("donnez un nbr "))
# for i in range(0,n+1):
#     y=y+i
# print("le résultat est :", y)

y=1
n=int(input("donnez un nbr "))
for i in range(1,n+1):
    y=y*i
print("le factoriel de ",n, " est :", y)
"""algo d'euclide"""
# a=int(input("donner a "))
# b=int(input("donner b "))
# c=max(a,b)
# d=(a+b)-c
# r=c%d
# while r!=0 :
#     c=d
#     d=r
#     r=c%d
# print("le PGCD est : ",d )
# p=(a*b)/d
# print("le PPCM est : ",p )
"""decomposition"""
# x=int(input("donnez le chiffre "))
# i=2
# while int(x/i) != 1:
#     if x%i==0:
#         print(x," divisble par ", i )
#         x=x/i
#         i=1
#         print(x)
#     i=i+1

# x= int( input('donnez le chiffre '))
# y= int( input('donnez le chiffre '))
# #print( x ,'mod',y ,' = ', x%y)
# print((x%y)-y)

# def facto(a,):
#     y=1
#     for i in range(1,a+1):
#         y=y*i
#     return y

# n=int(input("donner le nbr des chevaux partants "))
# p=int(input("donner le nbr des chevaux joués "))
# print("Dans l'ordre : une chance sur ",(facto(n)/facto(p)), "de gagner ")
# print("Dans le désordre: une chance sur ", facto(n)/(facto(n-p)*facto(p)), "de gagner ")

# def absolu(x):
#     if x<0:
#         v=-x
#     else:
#         v=x
#     return v 

# def dist(x,y,z):
#     i=0 
#     if x!=y:  
#         i=i+1
#     if x!=z :
#         i=i+1
#     if y!=z:
#         i=i+1
#     return i 
# a="hind"
# b=" moussaif"
# for i in range(1,10,2):
#     print("*"*i)

# pos=0
# n=int(input("donner un chiffre"))
# maxi=n
# i=1
# while n!=0 :
#     n=int(input("donner un chiffre "))
#     i+=1
#     if maxi<n :
#         maxi=n
#         pos=i
# print("le maximum est : ", maxi , " la position est : ", pos )




# s=1
# r=1
# t=1

# n=int(input(" nbr de chvx partants "))
# p=int(input(" nbr de chvx jouées "))
# for i in range(1,n+1):
#     s*=i
# for i in range(1,n-p+1):
#     r=r*i
# for i in range(1,p+1):
#     t=t*i
# x=round(s/t)
# y=round(s/(r*t))

# print(" dans l'ordre c est une chance sur  ", x,"  de gangner ")
# print( " dans le désrdre c est une chance sur : ", y , " de gangner ")

# def factorielle(a) :
#     y=1
#     for i in range( 1, a+1):
#         y=y*i
#     return y 


# n=int(input(" nbr de chvx partants "))
# p=int(input(" nbr de chvx jouées "))
# print(" dans l'ordre c est une chance sur  ", round(factorielle(n)/factorielle(n-p)),"  de gangner ")
# print( " dans le désrdre c est une chance sur : ", round(factorielle(n)/(factorielle(p)*factorielle(n-p))) , " de gangner ")

# def factorielle(n):
#     a=1
#     for i in range(1,n+1):
#         a=a*i
#     return a 
# def x(n,p):
#     return factorielle(n)/factorielle(n-p)
# def y(n,p):
#     return factorielle(n)/( factorielle(p)*factorielle(n-p) )
# n=int(input("donner le nbr des chvx partants "))
# p=int(input("donner le nbr des chvx joués "))
# print("dans l'ordre c est une chance sur :", x(n,p), " de gagner ")
# print( "dans le désorde c est une chance sur ", y(n,p) , "de gagner ")

# def rechercheB(n,liste):
#     if n not in liste:
#         return(-1)
#     else:
#         return liste.index(n)
# liste=[1,2,3,4,5,6,7]
# print(rechercheB(6,liste))

# n=int(input("donnez un chiffre "))
# n1=str(n)
# s=0
# for i in n1:
#     s=s+int(i)
# print(s)
# n = int(input("Choisissez un nombre supérieur à 2 : "))

# if(n>=2):
    
#     if(type(n/1) == int and type(n/n) == int):

#         print("C'est un nombre premier")

#     else:
        
#         print("Ce n'est pas un nombre premier")

# else:

#     print("Le chiffre n'est pas supérieur à 2")

#     n = int(input("Choisissez un nombre supérieur à 2 : "))

# n=4
# pseudo=input("donnez un pseudo ")
# while len(pseudo)<n:
#     pseudo=input("pseudo incrrect, donnez un autre ")
# print("Bonjour ", pseudo)


# nombre = input("Écris un nombre entier positif : ")
# nombre = int(nombre)
# i = 2
# while i < nombre and nombre % i != 0:
#     i = i + 1
# if i == nombre:
#     print("Le nombre", nombre, "est premier !")
# else:
#     print("Ce n'est pas un nombre premier.")

# def Premier(n):
#     i=2
#     while i < n and n % i !=0:
#         i= i + 1
#     if i == n:
#         return ("premier")
#     else :
#         return ("n'est pas premier.")
# print(Premier(2))

# n=input("saisir un pseudo ")
# while len(n)<4 :
#     n=input("pseudo incorrect, veuillez le saisir de nouveau: ")
# print( "Bonjour ", n, "!")

# def maxval(a,b):
#     if a>b:
#         return a
#     else:
#         return b 
# def minval(a,b):
#     if a<b:
#         return a
#     else:
#         return b 
# print(minval(1,4))

# nb = int(input("entrez un nombre afin de voir si c'est un nombre AMSTRONG : "))
# nbAmstrong = str(nb)
# resultat = 0
# for i in nbAmstrong:
#     resultat = resultat + ((int(i)**3))
# if resultat == nb:
#     print("Le nombre saisi est bien un nombre AMSTRONG")
# else:
#     print("Le nombre saisi n'est pas un nombre AMSTRONG")

# z=99
# for z in range(1000):
#     y=0
#     x=str(z)
#     for i in x:
#         y=y+(int(i)**3)
#     if y==int(x):
#         print(y)
# def estpremier(nombre):    
#     i = 2
#     while i < nombre and nombre % i != 0:
#         i = i + 1
#     if i == nombre:
#         return True
#     else:
#         return False   
# print(estpremier(13))
# def estpremier(n):
#     for i in range(2,n):
#         if (n%i != 0):
#             i+=1
#             return True
#         else:
#             return False

# def estpremier(n):
#     dividers = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             dividers.append(i)
#     return dividers == [1, n]
# def somchiffre(n):
#     return sum(int(r) for r in str(n))
# print(somchiffre(23452))
# def somchiffre(n):
#     r = 0
#     for i in str(n):
#         r += int(i)
#     return r
# print(somchiffre(23452))
"""recherchel"""
# def recherchel(t,n):
#     if n in t:
#         return t.index(n)
#     else:
#         return -1

# def recherchel(t,n):
#     for i in range(len(t)):
#         if t[i]==n:
#             return i
#     return -1


# t=[1,2,3,6,8]
# print(recherchel(t,3))
# f=0
# a=1
# for i in range(2,a):
#     r=a%i
#     if r==0:
#         f+=1
# if f!=0:
#     print("amst")
# else:
#     print("non")

"""palinndrome slam sqy"""
# def estpremier(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True 

# def estpremier(n):
#     i=2
#     while i<n and n%i!=0:
#         i+=1
#     if i==n: 
#         return True
#     else:
#         return False
# print(estpremier(10))
    
# def somchiffre(n):
#     n=str(n)
#     y=0
#     for i in n :
#         y+=int(i)
#     return y 

# def somchiffre(n):
#     return sum(int(r) for r in str(n))
# print(somchiffre(59))
l=["A","4","R","M"]
# def recherchel(q,l):
#     if q not in l :
#         return -1
#     else:
#         return l.index(q)

# def recherchel(l,p):
#     c=0
#     for i in l:
#         c+=1
#         if p==i:
#             return c-1
#     return -1

# def recherchel(l,p):
#     for i in range(0, len(l)):
#         if l[i]==p:
#             return i
#     return -1
# print(recherchel(l,"M"))
# t=[1,22,3,0]
# def maximum(l):
#     max=l[0]
#     for i in range(1,len(l)):
#         if max<l[i]:
#             max=l[i]
    
#     return max 
# print(maximum(t))

# n=int(input("entrez un nombre  "))
# u=n
# i=0
# while u!=1:
#     if (u%2==0):
#         u=u/2
#     else:
#         u=(u*3)+1   
#     i+=1
# print(i)

# n=int(input("entrez un nombre  "))
# u=n
# i=0
# while (u!=1):
#     if (u%2==0):
#         u=u/2
#     else:
#         u=(u*3)+1   
#     i+=1
# print("votre temps de vol saura de",i)

# a = str(input("Donnez votre identifiant "))
# if a=="bob":
#     b=int(input("donnez votre mot de passe"))
#     if b==1234:
#         c=input("la ville de naiss ")
#         if c=="Paris":
#             print("Bonjour")
#         else:
#             print(" c est faux ")
#     else:
#         print("mot de passe erroné ")
# else:
#     print("identifiant erroné ")
# a=input("donnez un identifiant ")
# if a!="bob":
#     print("identifiant erroné")
# elif a=="bob":
#     b = int(input("donnez le mot de passe"))
#     if b != 1234:
#         print("mot de passe errone")
#     else:
#         print("bonjour bob")


# n=int(input("entrer un nombre"))
# u=n
# i=0
# while u!=1:
#     if u%2==0 :
#         u=u/2
#     else:
#         u=u*3+1
#     i=i+1
# print(i)
l=["janvier","fevrier", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"]
# def mois(n):
#     if n==0:
#         return "0 n est pas accepter "
#     return l[n%12-1]
# import math

# def annee(n): 
#     return 2016 + math.floor((n-1) / 12)
# def annee(n):
#     return 2016+((n-1)//12)
# def s(n):
#     if n==1:
#         return 2000
#     else:
#         return s(n-1)*1.001+1
# def annee(n):
#     y = 2016
#     while n > 12:
#         y += 1
#         n = n-12
#     return y
# t=0
# n=0 
# while(t<3000):
#     n+=1
#     t=s(n)


# def mois(n):
#     return l[(n%12)-1]
# def annee(n):
#     return 2016+(n-1)//12
# def s(n):
#     if n==0:
#         return 2000
#     else:
#         return s(n-1)*1.001+1
# n=1
# while s(n)<= 3000:
#     n+=1
# print(" le salaire de paul dépasse les 3000 euros en ",mois(n)," ", annee(n))
"""bts blanc mlv"""
# def trouverlettre(n):
#     if n in l :
#         return l.index(n)
#     else:
#         return -1 

# l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# def codage(m):
#     long=len(m)
#     messagecode=""
#     for i in m:
#         rang=trouverlettre(i)
#         if rang==-1:
#             messagecode+=i
#         else:
#             rangcode=rang +13
#             if rangcode>25:
#                 rangcode-=26
#             lettreCode=l[rangcode]
#             messagecode+=lettreCode
#     print(messagecode)
#     return messagecode

# """list sqy1"""
# sqy=[10,21,13,4,53,6]
# def maximum(sqy):
#     maxi=sqy[0]
#     for i in range(1,len(sqy)):
#         if sqy[i] > maxi:
#             maxi=sqy[i]
#     return maxi
# print(maximum(sqy))

# mat=[[20,50,10],[0,50,100],[70,80,90]]
# def ecrire_mat(mat):
#     # for i in range(len(mat)):
#     #     print(mat[i])
#     for i in mat:
#         print(i)
# def lum(mat):
#     s=0
#     #b=0
#     for i in mat :
#         for j in i :
#             s+=j
#             #b+=1
#     return s/(len(mat)*len(i))


# # def contrastes(mat,m):
# #     for i in mat :
# #         for j in i:
# #             if j<m:
# #                 j=j//2
# #             else:
# #                 j=j*2
# #                 if j>100:
# #                     j=100
# #     return mat
# # m=lum(mat)

# mat=[[20,50,10],[0,50,100],[70,80,90]]
# luminosite= lum(mat)
# def contraste(mat, luminosite):
#     new_MAT = []
#     for ligne in mat:
#         new_ligne = []
#         for sat in ligne:

#             if sat < luminosite:

#                 new_ligne.append(sat //  2)

#             else:
#                 new_ligne.append(min(sat * 2,100))

#         new_MAT.append(new_ligne)

#     return new_MAT
# ecrire_mat(contraste(mat, lum(mat)))

"""13 AVRIL"""
mat=[[10,20,0],[20,50,100],[0,0,20]]

# def ecrire_matrice(mat):
#     for i in mat:
#         print(i)

# def luminosite(mat):
#     total=0
#     c=0
#     for i in range (len(mat)):
#         for j in range (len(mat[i])):
#             total+=mat[i][j]
#             c+=1
#     return total//c 

# def contraste(mat,m):
    
    
#     for i in range(len(mat)):
#         for j in range(len(mat[i])):
#             if mat[i][j]<m:
#                 mat[i][j]=mat[i][j]//2
#             else:
#                 mat[i][j]=min(mat[i][j]*2,100)
#     return mat

# m=luminosite(mat)
# ecrire_matrice(contraste(mat,m))
# mat=[[10,21,0],[20,55,100],[2,3,20]]
# def somme_impaire(mat):
#     s=0
#     for i in mat:
#         for j in i:
#             if j%2 != 0:
#                 s=s+j
#     return s

# def somme_paire(mat):
#     s=0
#     for i in mat:
#         for j in i:
#             if j%2 == 0:
#                 s=s+j
#     return s
            
# print(somme_paire(mat))
"""BTS BLANC SYRACUSE"""

# n=int(input("donnez une valeur superieure strictement à 0 "))
# while n<=0:
#     n=int(input("donnez une autre valeur superieure strictement à 0 "))
# u=n
# i=0
# while u!=1 :
#     if u%2==0 :
#         u=u//2
#     else:
#         u=u*3+1
#     i=i+1
# print("le temps de vol est ",i-1)
"""SQY1"""
def rechercheL(a,l):
    # for i in range(0,len(l)):
    #     if l[i]==a:
    #         return i
    for i in l :
        if i==a:
            return l.index(a)
    return -1
l=[1,2,94,7,59,10]
def maximum(l):
    maxi=l[0]
    for i in l:
        if maxi<i:
            maxi=i
    return ("le maximum est ", maxi, "son indice est ",l.index(maxi))
def somme(l):
    s=0
    for i in l:
        if i % 2 !=0:
            s=s+i
    return s
def extr(l):
    maxi=l[0]
    mini=l[0]
    for i in l:
        if maxi<i:
            maxi=i
        if mini>i:
            mini=i
    return "le max est " ,maxi, " le min est ", mini 
# pseudo=input("saisir un pseudo ")
# while len(pseudo)<4 :
#     pseudo=input("Pseudo incorrect, veuillez le saisir à nouveau ")
# print("Bonjour ",pseudo, " !")

mat=[[10,20,75],[100,50,0],[0,25,30]]
def ecrire_matrice(mat):
    for i in range(0,len(mat)):
        print(mat[i])

def luminosite(mat):
    s=0
    nbr_elem=0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            s+=mat[i][j]
            nbr_elem+=1 
    return (s/nbr_elem)
m=luminosite(mat)
def contraste(mat,m):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]<m:
                mat[i][j] //=2
            else:
                mat[i][j]=min(100,mat[i][j] *2)
    return mat 
print(contraste(mat,m))

    

