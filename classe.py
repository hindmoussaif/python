#__________________________________________propriétés,edition et acces au attributs_______________________________________________________
# class Personne :
#     """classe personne ayant 4 attributs :
#     nom, prenom, age ,lieu_de_residance"""

#     def __init__(self,nom,prenom):
#         self.nom=nom
#         self.prenom=prenom
#         self.age=26
#         self._lieu_de_residance='Paris'
        
#     def grandir(self,annee):
#         self.age+=annee

#     def _get_lieu_residance(self):
#         # print('Nous affichons le lieu de residance!')
#         return self._lieu_de_residance

#     def _set_lieu_residance(self,nouvelle_residance):
#         print('il semble que {} deménage à {} '.format(self.nom,nouvelle_residance))
#         self._lieu_de_residance=nouvelle_residance
    # def __del__(self):
    #     print("vous avez supprimer le compte de {} ".format(self.nom)) 
    #     """ la methodes del permet de visualiser la suppression des objet
    #     les objet sont supprimer(tuée) soit explicitement durant l'execution ou à la fin du programme)"""

    # # def _set_lieu_residance(self,nouvelle_residance):
    #     a=input('donnez un mot de passe pour changer l\'adresse')
    #     a=int()
    #     if a==2020:
    #         self._lieu_de_residance=nouvelle_residance
    #     else:
    #         print('mot de passe incorrecte')

#     def __repr__(self):
#         """cette methode affiche les attributs"""
#         return "Personne: nom({}) ,prenom({}), age({}) , lieu_de_residance({})".format(self.nom,self.prenom,self.age,self._lieu_de_residance)

#     def __str__(self):
#         """permet d afficher joliment les attributs de l'objet"""
#         return " {} {} , agé de {} ans habite actuellement à {}  ".format(self.nom, self.prenom, self.age,self.lieu_de_residance)

#     def __getattr__(self,nam):
#         """cette methode renvoie une alerte si l attribut n'existe pas"""
#         print("Alerte!! aucune information sur la/le {} de {} {}  !".format(nam,self.nom,self.prenom))
    
#     def __setattr__(self,mon_attribut,ma_valeur):
#         object.__setattr__(self,mon_attribut,ma_valeur)
#         print("daz men hna : ",mon_attribut,ma_valeur)

#     lieu_de_residance=property(_get_lieu_residance,_set_lieu_residance)
    
# hind = Personne('asri','hind')
# hind.nom='moussaif'
# ayoub=Personne('asri','ayoub')
# print(hind)
# print(hind.nom)
# ayoub.profession

#___________________________________communication entre classes______________________________________________________________


# class TableauNoire:

#     def __init__(self,personne):#le constructeur de la classe TableauNoire pour cree des espaces
#         self.surface=''
#         self.proprietaire =personne


#     def ecrire(self,message):#methode ecrire pour ecrire sur la surface du taleau
#         if self.surface!='':
#             self.surface+=('\n')
#         self.surface+=message
#     def lire(self):
#         print(self.surface)
#     def effacer(self):
#         self.surface=''
# tab=TableauNoire(hind)
# tab.ecrire('bonjour les classes')
# tab.lire()
# tab.ecrire('ca avance bien elhamdolilah')
# tab.lire()
# tab.effacer()
# tab.ecrire('je souhaite terminer ce matin')
# tab.lire()
# print(tab.proprietaire)


#__________________________________________variables et methodes de class_______________________________________________________

# class Compteur:
#     objet_cree = 0
#     def __init__(self,nom):
#         Compteur.objet_cree+=1 #nomdeclasse.attributdeclasse
#         self.nom=nom #self.attribut d objet  
#     def combien(cls):#methode de class prend cls comme parametre et non pas self(cls classe, self objet)
#         print("vous avez cree {} objet " .format(cls.objet_cree))
#     combien=classmethod(combien) #la syntaxe pour declarer une methode de classe alors il utilisera que les attributs de la classe 
# Compteur.combien()
# hind=Compteur('hind')
# print(hind.nom)
# hind.combien() #on peut appeler une methode de class par un objet deja crée 
# a=Compteur('mahjoub')
# print(a.nom)
# Compteur.combien()
# b=Compteur('aicha')
# print(b.nom)
# c=Compteur('ayoub')
# print(c.nom)
# Compteur.combien()


#______________________________________________methode statique ___________________________________________________

# class test:
#     def afficher():
#         print("c est une fonction statique, alors elle fait le meme traitement independanement des cntenus des objets")
#         print("sa definition est comme la methode de classe ")
#     afficher=staticmethod(afficher) #nomdemethod=staticmethod(nomdemethode)
# test.afficher() #pour appeler la methode on met nomdeclass.nomdemethode

#_____________________________les methodes de conteneur____________________________________________________________________
class Dicto:
    """notre class va enveloper des dictionnaires"""
    def __init__(self):
        """ce constructeur n'aura pas de paramétres"""
        self._dictionnaire={}
    def __getitem__(self,index):
        """cette fonction special nous permet d'acceder à self._dictionnaire[index] en tapant objet[index]"""
        return self._dictionnaire[index]
    def __setitem__(self,index,value):
        """cette methode est appeler quan on ecrit objet[index]=value pour retournet self._dictionnaire[index]=value"""
        self._dictionnaire[index]=value
    def __contains__(self,value):
        """ cette fonction permet de personaliser le renvois de (in) """
        a= value in self._dictionnaire.values() 
        b= value in self._dictionnaire.keys() 
        if a==True and b==True:
            print('le nbr {} existe dans les valeurs et les clés !!  '. format(value))
        elif a==True and b==False:
            print("le nbr {} existe, c est une valeur du dictionnaire".format(value))
        elif b==True and a==False:
            print("la nbr {} n\'existe pas dans les valeur,mais il existe dans les clé du dictionnaire  ".format(value))
        else:
            print("le nbr {} n\'existe ni dans les valeurs ni dans les clés ".format(value))
    def __len__(self):
        print("la longueur de votre objet est  ")
        return len(self._dictionnaire)
        
    
dic=Dicto()
dic[0]=10
dic[1]=20
dic[2]=25
dic[10]=30
0 in dic
10 in dic
20 in dic
40 in dic

#______________________________________methodes mathématiques___________________________________________________________

# class Duree:

#     def __init__(self,min=0,sec=0):
#         self.min=min
#         self.sec=sec
#         self.attribut_temporaire=5
#     def __str__(self):
#         if self.sec >= 60:
#             self.min += self.sec // 60
#             self.sec = self.sec % 60
#         return '{00:02}:{01:02}'.format(self.min,self.sec)
# #les opérateurs mathématique (+ - * / // %  ......) ne sont pas suppoter pour le type durée alors il faut les définir 
#     def __add__(self,value):
#         da=Duree()
#         da.min=self.min
#         da.sec=self.sec
#         da.sec += value        
#         if da.sec >= 60:
#             da.min += da.sec // 60
#             da.sec = da.sec % 60            
#         return da
# #les opérateurs de comparaison( == > >= < <= != ) ne sont pas suppoter pour le type durée alors il faut les définir 
#     def __ge__(self,obj):
#         if self.min>=obj.min:
#             a=True
#         elif self.min==obj.min and self.sec>=obj.sec:
#             a=True
#         else:
#             a=False
#         return a
# #getstate et setstate sont à utiliser si on veut utiliser la class pickle 
# #getstate permet de pickler / setstate permet de unpickler 
#     def __getstate__(self):
#         """Renvoie le dictionnaire d'attributs à sérialiser"""
#         dict_attr = dict(self.__dict__)
#         """ on crée un objet de la classe dictionnaire """
#         dict_attr["attribut_temporaire"] = 0
#         return dict_attr
#     def __setstate__(self, dict_attr):
#         """Méthode appelée lors de la désérialisation de l'objet"""
#         dict_attr["attribut_temporaire"] = 0
#         self.__dict__ = dict_attr
# # #execution
# d1=Duree(1,67)
# print(d1)
# d2=d1+45
# print(d2)
# d2+=10
# print(d1.attribut_temporaire)
# print(d2)
# print(d2>=d1)
# d1.attribut_temporaire=7
# print(d1>=d2)
# print(d1.attribut_temporaire)
#______________________________________Résumé ___________________________________________________________
"""Les méthodes spéciales permettent d'influencer la manière dont Python accède aux attributs 
d'une instance et réagit à certains opérateurs ou conversions.

Les méthodes spéciales sont toutes entourées de deux signes « souligné » (_).

Les méthodes__getattr__,__setattr__et__delattr__contrôlent l'accès aux attributs de l'instance.

Les méthodes__getitem__,__setitem__et__delitem__surchargent l'indexation ([]).

Les méthodes__add__,__sub__,__mul__… surchargent les opérateurs mathématiques.

Les méthodes__eq__,__ne__,__gt__… surchargent les opérateurs de comparaison."""