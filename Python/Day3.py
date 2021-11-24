# Python Programming  - Day 3

print("Hello World!")

#--------------------------------------------------------------------------------------------------------------------------------

# if else condition

print("Welcome to love matrimonial")
age = int(input("Enter your age to login: "))
if age >18:                                            # <, >, <=, >=
    print("You are eligible for love")
else:
    print("Small boy you are not eligible")

#--------------------------------------------------------------------------------------------------------------------------------

#Exercise

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number %2 == 0:                      # % modulo will print the output of reminder
  print("The given number is even")
else:
  print('The given number is odd')

#--------------------------------------------------------------------------------------------------------------------------------

  #Nested if statement

print("welcome to online Learning platform")
age = int(input("Enter your age here: "))
if age > 20:
    print("Yor are eligible to learn higher studies")
    if age >=25:
        print("You are eligible to apply membership card")
    elif age < 25:
        print("you are eligible for junior membership")
    else:
        print("You are not eligible")
else:
    print("Your age must not reachable")


# Exercise:-

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

#--------------------------------------------------------------------------------------------------------------------------------

#Excercise:- 2

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Refer to the flow chart here: https://bit.ly/36BjS2D
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#------------------------------------------------------------------------------------

#Multiple if statement (Roolercoaster)

print("Welcome to the RollerCoaster")
height = int(input("Enter your correct height: "))
bill=0

if height >=120:
    print("You are eligible for the ride, enjoy")
    age=int(input("Enter your age to enjoy the ride: "))
    if age < 12:
        bill=5
        print("You have to pay 5$")
    elif age <=18:
        bill=7
        print("You have to pay 7$")
    else:
        bill=12
        print("You have to pay 12$")
    photo = input("Do you want to take photo? Y or N. ")
    if photo == "y":
        bill = bill + 3   # bill += 3
        print(f"Your final bill is {bill}")
else:
    print("You're height not support to enjoy the ride")


#-------------------------------------------------------------------------------------

# Pizza Order Excercise

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")

#-------------------------------------------------------------------------------------

# Logical Operator

# A and B  both the statement will be true
# A or B   either 1 of true is enough
# not A    True statement changed to False

#---------------------Excercise------------------------------

# Love Calculator

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


#--------------------------------------------------------------

# Treasure Game Project

print("Welcome to treasure island")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("I Welcome you again to the treasure island, your mission is to find the treasure using right path")
print("Have a fun to play the game")
name = input("Please enter your name for playing the game: ").upper()
choice1 = input('You\'r are in the island now, choose "left" or "right" to continue the game: ').lower()
if choice1 == str("left"):
    choice2 = (input('''Welcome, You successfully completed Level-1. 
                    Now you are in middle island:- Choose 'swim' or 'wait' to complete level-2: ''')).lower()
    if choice2 == str("wait"):
        choice3 = input('''Congrats, you crossed level-2. Its time to choose the door in front of you.
                 Choose any one colored door "Red" or "blue" or "Yellow" to get the treasure: ''').lower()
        if choice3 == 'red':
            print("The red color room full of fire, Game Over")
        elif choice3 == "blue":
            print("The blue colored room full of water, Game Over")
        elif choice3 == 'yellow':
            print(f"Wow, {name} Excellent You find the treasure. Congrats.........................")
        else:
            print("you choosen door not exit. Fuck You!...")
    else:
        print("Oh, oh you choose wrong decision. You are hunted by sea animals. Game Over!.....")
else:
    print("Oh, oh you choosen a wrong direction. You fellow down in to the hole :--: Game Over!....")

#---------------------------------------------------------------

# Python Program using Food Tip Calculator

print('''
Restaurant
                     ________
             <<<|>> |PARADISE|
               _|___|[] [] []|
              |[] []|        |
   ___________|_____|[]_[]_[]|_
  |                            |
  |   <>   CAFE  LAMOUR   <>   |
  |____________________________|
 /::::::::::::::::::::::::::::::\
/::::::::::::::::::::::::::::::::\
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
 |  _______________   _________ |\.--------.
 | |vvv|vvv|vvv|vvv|  || _ _ || | | Hotel  |
 | |   |   |   |   |  |||_|_||| | |Entrance|__
 | |%%%+%%%+%%%+%%%|  |||_|_||| |/'--------'
 | |%%%|%%%|%%%|%%%|  ||     || |
 | |%%%|%%%|%%%|%%%|  ||o    || |()         ()
 |  """""""""""""""   ||     || ||| /     \ ||
 |                    ||_____|| |||/       \||lc
 ~~~~~~~~~~~~~~~~~~~~~/_______\~~ /         \

~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.<>.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~.:.~
''')

print("Welcome to Chinnu Restaurant")
# total bill
# Tips
#How many people shares

bill = float(input("Enter the total amount of cost you have to pay: $"))
tips = int(input("Please provide tips for waiter, tips will be '10', '12' or '15'. Enter tips: $"))
people = int(input("Enter how many peoples were going to share the cost: $"))

average_tips = float(bill * tips /100)
final_tips = int(bill + average_tips)
total_amount = final_tips / people
print(int(total_amount))
