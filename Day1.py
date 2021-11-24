# PYTHON PROGRAMMING - DAY_1

print("Hello World!") #print hello world!

#-------------------------------

#print the given statement exactly without any change
print("Day 1 - Python Print Function")
print('The function is declared like this: ')
print("print('What to print')")  # here we can use [" ' ' "]

#-------------------------------

#we have to give space between the hello & Chinnu
print("Hello" + "Chinnu")
print("Hello " + "Chinnu")      #step1 ("Hello ")
print("Hello" + " Chinnu")      #step2 (" Chinnu")
print("Hello" + " " + "Chinnu") # step3 (+ " " +)

#-------------------------------

#Debug the code
#-----------------#
#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.)
# print('e.g. print("Hello" + "World")')
#print(("New lines can be created with a backslash and n.")

# Correct answer 
print("Day 1 - String Manipulation") # Missing double quotes before the word day. 
print('String Concatenation is done with the "+" sign.') # Outer double quotes changed to single quotes.
print('e.g. print("Hello" + "World")') # Extra identication removed.
print("New lines can be created with a backslash and n.") # Extra ( in print function removed.

#-------------------------------

# Asking input from the user

# Step-1
print("Hello " + input("What's your name? ") + "!")   # Getting input from the user

# Step-2
x=input("What's your name? ")  # we assign variable to get input. The variable is X
print(x)

# Step-3
x=input("What's your name? ") # we assign variable to get input. The variable is X
print(x)
print("Hello" + " " + x)

#-------------------------------

x=input("What's your name? ") #Getting input from user
print(len(x))  #calculate the length of the user's input

#-------------------------------

#Variable
name=input("What's your name? ")  # we assign variable to get input. The variable is X
print(name)

#print text in next line \n
name = input("What is your name? ")
age = input("please enter your age: ")
#print(name)
#print(age)

print("Your name is: \n" + name + "\n" + "Your age is: \n" + age)


#------------Exercise------------#

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

x=a # create new variable and store a value in that
a=b # store b value in a
b=x # fix b value as newly created variable (that the x contain a value)


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#--------------Final_Excerise--------------#

print("Welcome to the Band Name Generator.")
city_name = input("What's name of the city you grew up in?\n" ) # (\n) is used to print the text in next line
pet_name = input("What's your pet's name?\n")
print("your band name could be " + city_name + " " + pet_name)
