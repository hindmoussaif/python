"""day1 : band name generator """
# #1. Create a greeting for your program.
# #2. Ask the user for the city that they grew up in.
# a=input("Welcome to the Band name Genarator \nWhat's name of the city you grew up in?\n")
# #3. Ask the user for the name of a pet.
# b=input("what's the name of your first pet ?\n")
# #4. Combine the name of their city and pet and show them their band name.
# print("the name of your brand is the "+a+" "+b)
"""day 2 tip calculator """
print("Hello to the tip calculator ")
a=float(input("What was the total bill? "))
p=int(input("How much tip would you like to give? 10, 12, or 15? "))
p/=100
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
n=int(input("How many people to split the bill? "))
r=round((a/n)*(1+p),2)
print("Each person should pay: $",r)





