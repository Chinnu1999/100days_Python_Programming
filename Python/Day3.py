                                     # Python Programming
                                            # Day-3

# Conditional if / else

print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm? "))
if height > 120:
  print("You can enjoy the ride!")
else:
  print("Sorry, your height is not taller. So, you are not allowed!")

# Comparison Operators

# >   -> Greater than
# <   -> Lesser than
# >=  -> Greater than or equal to
# <=  -> Lesser than or equal to
# ==  -> Equal to
# !=  -> Not equal to  

# [ difference between = and ==, = is used to assign values into the variables but == is used to check the equality between left and right values.]


# Exercise - 1

# Write a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder.

# Answer:
  
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

if number % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")

#-------------------------------------------------------------------------------------------

# Nested if statement

print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm? "))
if height > 120:
  print("You can enjoy the ride!")
  age = int(input("What is  your age? "))
  if age>18:
      print("Your ride cost is $12")
  else:
      print("Your ride cost is $7")
else:
  print("Sorry, your height is not taller. So, you are not allowed!")

#--------------------------------------------------------------------------------------------------------------------------------
# elif statement

print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm? "))
if height > 120:
  print("You can enjoy the ride!")
  age = int(input("What is  your age? "))
  if age<12:
      print("Your ride cost is $5")
  elif age>18:
      print("Your ride cost is $12")
  else:
      print("Your ride cost is $7")
else:
  print("Sorry, your height is not taller. So, you are not allowed!")

#------------------------------------------------------------------------------------------

# Excercise - 2

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
  
# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.


# Answer: 
  
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

BMI =round(weight / (height * height))

if BMI <18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI <25:
  print(f"Your BMI is {BMI}, You have a normal weight")
elif BMI <30:
  print(f"Your BMI is {BMI}, You have Overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI}, You have Obese")
else:
  print(f"Your BMI is {BMI}, you are clinnically obese.")

#--------------------------------------------------------------------------------------------------------------------------------

# Excercise - 3:

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)
  
# Answer:
  
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")


#-------------------------------------------------------------------------------------------

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

# Excercise - 4

# Pizza Order

#you've got a job at Python Pizza. Your first job is to build an automatic pizza order program. Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20  
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
  
# Answer:

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆  
bill =0


if size == "S":
  bill = bill + 15
elif size == "M":
  bill = bill + 20
else:
  bill = bill + 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.") 


#---------------------------------------------------------------------------------------------

# Logical Operator

# A and B  both the statement will be true
# A or B   either 1 of true is enough
# not A    True statement changed to False

print("Welcome to the RollerCoaster")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
  print("You can enjoy the ride!")
  age = int(input("What is  your age? "))
  if age<12:
      bill =5
      print("Child ticket cost is $5")
  elif age<=18:
      bill =7   
      print("Youth ticket cost is $7")
  elif age>=45 and age <=55:
      bill = 0
      print("Your ticket cost is $0")
  else:
      bill =12
      print("Adult ticket cost is $12")
      
  photo = input("Do you want to take photo? Y or N ")
  if photo == "Y":
      bill = bill + 3
  print(f"your final bill is {bill}")         
else:
  print("Sorry, your height is not taller. So, you are not allowed!")


# Excercise - 5

# Love Calculator

#You are going to write a program that tests the compatibility between two people. To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
#"Your score is **z**."

 
# Answer:

  # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆  
  
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


