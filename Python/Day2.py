# PYTHON PROGRAMMING - DAY_2

# Data Types:-
              # 1. Strings (just a character)

print("Hello World!" [0])    # Hello World!    
                              # 01234567891011  (Check the string character)
                              # ..........-2-1  (Check the string in reverse order)
# [1....] by using square bracket with inside some number is dissect the stirng by individual character

print("Chinnu"[-2])  # check character in -2(string)

              # 2. Integers (Numbers with Positive & Negative)

print(123+211)

              # 3. Floating Point (.)

print(3.14159 + 1)

             # 4. Boolean

print(True)
print(False)

#---------------------------------------------------------------------------------

#Type Error, Type Check & Type Conversion

#Type Error & Type Conversion
a=len(input("What's your name? "))   # Check how many characters are there from input 
b=str(a)         # Convert integer into string(because concatenate str (not into) to str)
print('Your name as ' + b + ' characters.')
                      # you can convert str to int or str to float or float to str

#Type Check
a=input("Your Age: ")
print(type(a))           # Tyoe denote which data type we use (Here its string)

#-----------------------------------------------------------------------------------

#Excercise

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
# print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits togeter
two_digit_number = first_digit + second_digit

print(two_digit_number)

#-------------------------------------------------------------------------------------

#Mathematical Operators

print(3 + 5)   # addition 
print(10 -3)   # Subtract
print(5 / 2)   # Division
print(1 * 10)  # Multiply
print(3 ** 4)  # exponention (where 3 power 4 = 3*3*3*3)

# here we use PEMDAS rule (left to right)
  # ()
  # **
  # */
  # +-

print(3 * 3 + 3 / 3 -3 )  
# (3*3)=9 
# (3/3)=1 ---------------> (9+1-3)
# (10-3)    =======>>    ans=7

print(3 * (3 + 3) / 3 -3 )   # Answer = 3

#-------------------------------------------------------------------------------------

#Excercise

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)

#-------------------------------------------------------------------------------------

# Number Manipulation 

print(8 / 3) # 2.6666666666666665

print(round(8/3)) # 3 (here it  will round the number 2.666 to 3 )

print(round(8/3, 2)) # 2.67 (that 2 indicates .66666 convert to .67 )

print(8 // 3) # 2 (// - floor division it remove the decimal points )

result = 4/2
result /= 2        # (/= is dvided AND) used to divide again 
print(result)

#(we can use also +=, -=, *=, /= ......)

                              # f-string
                              #----------
score = 0
height = 6.5
award = True
print(f"your score is: {score}, your height is: {height}, your award is: {award}") # avoid use more lines we use f-string here)

#-------------------------------------------------------------------------------------

#Exercise

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#----------------------------------------------------------------------------------------------------







