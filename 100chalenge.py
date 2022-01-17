"""day1 : band name generator """
# #1. Create a greeting for your program.
# #2. Ask the user for the city that they grew up in.
# a=input("Welcome to the Band name Genarator \nWhat's name of the city you grew up in?\n")
# #3. Ask the user for the name of a pet.
# b=input("what's the name of your first pet ?\n")
# #4. Combine the name of their city and pet and show them their band name.
# print("the name of your brand is the "+a+" "+b)
"""day 2 tip calculator """
# print("Hello to the tip calculator ")
# a=float(input("What was the total bill? "))
# p=int(input("How much tip would you like to give? 10, 12, or 15? "))
# p/=100
# #If the bill was $150.00, split between 5 people, with 12% tip. 
# #Each person should pay (150.00 / 5) * 1.12 = 33.6
# n=int(input("How many people to split the bill? "))
# r=round((a/n)*(1+p),2)
# print("Each person should pay: $",r)
"""day 3 treasure """
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.") 
# a=input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')
# if a.lower()=="right":
#     print("Game over ")
# else:
#     b=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n')
#     if b.lower()=='swim':
#         print("Game over ")
#     else:
#         c=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
#         if c.lower()=="blue" or c.lower()=="red":
#             print("Game over")
#         else:
#             print("you win! ")
# """day 4 """
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
jeu=[rock,paper,scissors]
# user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# user_hand=jeu[user_choice]
# computer=random.randint(0,2)
# dev_choice=jeu[computer]
# print(user_hand,"\nComputer chose:\n",dev_choice)
# if (user_choice==0 and computer==2) or(user_choice==2 and computer==1) or (user_choice==1 and computer==0):
#     print("*********You win!*************** ")
# elif (user_choice==2 and computer==0) or(user_choice==1 and computer==2) or (user_choice==0 and computer==1):
#     print("**********You lose*****************")
# else:
#     print("************equal************")


""""day 5 password generator"""
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#methode1
# pw=""
# for i in range(0,nr_letters):
#     pw+=random.choice(letters)
# for i in range(0,nr_symbols):
#     pw+=random.choice(symbols)
# for i in range(0,nr_numbers):
#     pw+=random.choice(numbers) 
# print(pw) 
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# pwd="".join(random.sample(pw,len(pw)))
# print(pwd)
#Methode2
# pw=[]
# for i in range(0,nr_letters):
#     pw+=random.choice(letters)
# for i in range(0,nr_symbols):
#     pw+=random.choice(symbols)
# for i in range(0,nr_numbers):
#     pw+=random.choice(numbers)
# random.shuffle(pw)
# pwd=""
# for i in pw:
#     pwd+=i 
# print(pwd)

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while not( at_goal()):
#   if right_is_clear():
#      turn_right()
#      move()
#   elif front_is_clear():
#        move()
#   else:
"""day 7 hangman"""
# import random
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# def to_word(l):
#     w=""
#     for i in l:
#         w+=i
#     return w
# words=["baboon","caramel","hindouch"]
# chosen=random.choice(words)
# blank=[]
# for i in range(0,len(chosen)) :
#     blank.append("- ")
# print("your word is ",to_word(blank))

# n=int(input("choisi le niveau du jeu : 1: \"difficile\",2: \"moyen\",3: \"facile\" "))
# while n>3 or n<0:
#     n=int(input("choisi un des 3 niveaux proposés "))
# if n==1:
#     life=6
# elif n==2:
#     life=4
# else:
#     life=2

# found=to_word(blank)    
# j=0
# while found!=chosen and life!=0:
#     x=input("donnez une lettre ").lower()
#     if x in(chosen):
#         print(stages[j])
#         for k in range(0,len(chosen)):
#             if chosen[k]==x:
#                 blank[k]=x 
#         found=to_word(blank)  
#         print(found)
#     else:
#         j+=1
#         print(stages[j])
#         found=to_word(blank)
#         print(found)
#         life-=1
# if found==chosen:
#     print("greaat you saved my life ")
# else:
#     print(" you killed me !!!! ")
"""day 8 """
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def cesur(text,shift,direction):
#     code=""
#     for i in text:
#         if direction=="encode":
#             if i in alphabet:
#                 index=(alphabet.index(i)+shift)%26
#                 code+=alphabet[index]
#             else:
#                 code+=i
#         else:
#             if i in alphabet:
#                 index=(alphabet.index(i)-shift)%26
#                 code+=alphabet[index]
#             else:
#                 code+=i
#     return code
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
# print(cesur(text,shift,direction))
# again=input("type \"yes\" if you wanna go again otherwise type \"no\"" ).lower()
# while again=="yes":
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     print(cesur(text,shift,direction))
#     again=input("type \"yes\" if you wanna go again otherwise type \"no\"" ).lower()
"""day 9 """
# print("hello for biding ")
# bid={}
# a=input("give ur name ")
# b=int(input("how much u wanna bid : $"))
# c=input("is there any other bider \"yes\" or \"no\" :").lower()
# bid[a]=b
# max=b
# winner=a
# while c=="yes":
#     a=input("give ur name ").lower()
#     b=int(input("how much u wanna bid : $"))
#     while a in bid:
#         a=input("sonner un autre nom , celui la existe déja ").lower()
#     bid[a]=b
#     if max<b:
#         max=b
#         winner=a
#     c=input("is there any other bider \"yes\" or \"no\" :").lower()
# print("the winner is ,",winner,"with a bid of ", max,"$")  
"""day 10"""
# def add(a,b):
#     return a+b
# def soustract(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# a=int(input("what's the forst number "))
# o=input("choose an operator : \n+\n-\n*\n/ ")
# b=int(input("what is teh seconde number "))
# def calculator(a,o,b):
#     op={"+": add(a,b),"-":soustract(a,b) ,"*":multi(a,b),"/":div(a,b) }
#     if o in op:
#         print(a,o,b,"=",end="")
#         return op[o]
#     else:
#         print("operator error ")
#         return 0
# result=calculator(a,o,b)
# print(result)
# again=input("type'y' to continue calculating with {result} , or 'n' to start a new calculation or 'q' to quit : ").lower()
# while again!='q':
#     if again=='y':
#         a=result
#         o=input("choose an operator : \n+\n-\n*\n/ ")
#         b=int(input("what is teh seconde number "))
#         result=calculator(a,o,b)
#         print(result)
#     else:
#         a=int(input("what's the forst number "))
#         o=input("choose an operator : \n+\n-\n*\n/ ")
#         b=int(input("what is teh seconde number "))
#         result=calculator(a,o,b)
#         print(result)
#     again=input("type'y' to continue calculating with {result} , or 'n' to start a new calculation or 'q' to quit : ").lower()
"""day 11 jack card """
# import random
# start=input("press'y' to play an 'n' to quit ")
# def score(l):
#     score=0
#     for i in l:
#         score+=i
#     for i in l:
#         if i==11 and score>21:
#             score=score-10
#     return score
# while start=='y':
#     card=[11,2,3,4,5,6,7,8,9,10,10,10,10]
#     p=[random.choice(card),random.choice(card)]
#     d=[random.choice(card)]
#     pscore=score(p)
#     dscore=score(d)
#     print("     your cards ",p,", current score: ",pscore)
#     print( "    the dealer first card",d,"his score is ",dscore)
#     hint=input("do u wanna take an other card 'y' or 'n'").lower()
#     if hint=='y':
#         p.append(random.choice(card))
#         pscore=score(p)
#         print("     your cards ",p,", current score: ",pscore)
#         print( "    the dealer first card",d,"and his score is ",dscore)
#     d.append(random.choice(card))
#     dscore=score(d)
#     print(dscore)
#     if dscore<17:
#         d.append(random.choice(card))
#         dscore=score(d)
#     print("    your cards ",p,", current score: ",pscore)
#     print( "    the dealer last card",d," and last scor ",dscore)
#     if pscore>21:
#         winner="dealer"
#     elif dscore>21:
#         winner="me"
#     elif 21-pscore<21-dscore:
#         winner="me"
#     elif 21-pscore>21-dscore:
#         winner="dealer"
#     else:
#         winner="egualite"
#     print("****************** The winner is ",winner,"*********************")
#     start=input("press'y' to play an 'n' to quit ")
"""day 12 """
# import random
# print("Welcome to the number guessing game! \nI'm thinking of a number between 1 and 100.")
# C=random.randint(1,101)
# n=input("Choose a difficulty.Type 'easy' or 'hard'").lower()
# while n!="hard" and n!='easy':
#     n=input("Choose a difficulty.Type 'easy' or 'hard'").lower()
# def niveau(n):
#     if n=="hard":  
#         return 5
#     else: return 10   
# turn=niveau(n)
# def guess(turn):
#     global g
#     g=int(input("make a guess: "))
#     if g>C:
#         print("Too hight.\nGuess again.")
#     elif g<C:
#         print("Too low.\nGuess again.")
#     else:
#         print("Good job you win the number is :",C)
# print("you have ",turn,"chance")
# guess(turn)
# while g!=C and turn >1:
#     turn-=1
#     print("you still have ",turn,'chances')
#     guess(turn)
# if turn==0:
#     print("You've run out of guesses, you lose.")
# again=input("do u wanna play again 'y' or 'no' ")
# def game():
#     C=random.randint(1,101)
#     n=input("Choose a difficulty.Type 'easy' or 'hard'").lower()
#     while n!="hard" and n!='easy':
#         n=input("Choose a difficulty.Type 'easy' or 'hard'").lower()
#     turn=niveau(n)
#     print("you have ",turn,"chance")
#     guess(turn)
#     while g!=C and turn>1:
#         turn-=1
#         print("you still have ",turn,'chances')
#         guess(turn)
#     if turn==0:
#         print("You've run out of guesses, you lose.")
# while again=="y":
#     game()
#     again=input("do u wanna play again 'y' or 'no' ").lower()
"""day 14 """
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 172,
        'description': 'Reality TV personality and businesswoman and Self-Made Billionaire',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 167,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 149,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 145,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 138,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'National Geographic',
        'follower_count': 135,
        'description': 'Magazine',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 133,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 131,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 127,
        'description': 'Reality TV personality and Model',
        'country': 'United States'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 119,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Nicki Minaj',
        'follower_count': 113,
        'description': 'Musician',
        'country': 'Trinidad and Tobago'
    },
    {
        'name': 'Nike',
        'follower_count': 109,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 108,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 107,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 94,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 90,
        'description': 'Reality TV personality',
        'country': 'United States'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 89,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 87,
        'description': 'Comedian',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 86,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 85,
        'description': 'Football club',
        'country': 'Spain'
    },
    {
        'name': 'Rihanna',
        'follower_count': 81,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 80,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': "Victoria's Secret",
        'follower_count': 69,
        'description': 'Lingerie brand',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 68,
        'description': 'Actress and musician',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 66,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Drake',
        'follower_count': 65,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 64,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 63,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 62,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 67,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'David Beckham',
        'follower_count': 82,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 61,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Justin Timberlake',
        'follower_count': 59,
        'description': 'Musician and actor',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 58,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'NASA',
        'follower_count': 56,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Emma Watson',
        'follower_count': 56,
        'description': 'Actress',
        'country': 'United Kingdom'
    },
    {
        'name': 'Shawn Mendes',
        'follower_count': 57,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 55,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Gigi Hadid',
        'follower_count': 54,
        'description': 'Model',
        'country': 'United States'
    },
    {
        'name': 'Priyanka Chopra Jonas',
        'follower_count': 53,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': '9GAG',
        'follower_count': 52,
        'description': 'Social media platform',
        'country': 'China'
    },
    {
        'name': 'Ronaldinho',
        'follower_count': 51,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Maluma',
        'follower_count': 50,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Camila Cabello',
        'follower_count': 49,
        'description': 'Musician',
        'country': 'Cuba'
    },
    {
        'name': 'NBA',
        'follower_count': 47,
        'description': 'Club Basketball Competition',
        'country': 'United States'
    }
]

logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
i=0
print(logo)
A=data[i]['follower_count']>data[i+1]['follower_count']
B=data[i]['follower_count']<data[i+1]['follower_count']
print(" compare A: ",data[i]['name'],data[i]['description'],data[i]['country'])
print(vs)
print("compare B : ",data[i+1]['name'],data[i+1]['description'],data[i+1]['country'])
reponse=input("tapez 'A' ou 'B' ").lower()
c=0
while ((reponse=="a" and A) or (reponse=='b' and B)) :
    c+=1
    i+=1
    print(" compare A: ",data[i]['name'],data[i]['description'],data[i]['country'])
    print(vs)
    print("compare B : ",data[i+1]['name'],data[i+1]['description'],data[i+1]['country'])
    reponse=input("tapez 'A' ou 'B' ").lower()
print("Votre score est :",c)