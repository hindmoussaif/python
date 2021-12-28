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
"""day 4 """
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
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
user_hand=jeu[user_choice]
computer=random.randint(0,2)
dev_choice=jeu[computer]
print(user_hand,"\nComputer chose:\n",dev_choice)
if (user_choice==0 and computer==2) or(user_choice==2 and computer==1) or (user_choice==1 and computer==0):
    print("*********You win!*************** ")
elif (user_choice==2 and computer==0) or(user_choice==1 and computer==2) or (user_choice==0 and computer==1):
    print("**********You lose*****************")
else:
    print("************equal************")



