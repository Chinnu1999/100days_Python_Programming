                                                                     # Python Programming
                                                                           # Day-1

print("Hello Ayyappan!..")   #printing  hello
# print is used to printing the data given by the user
# " " is used to remove unwanted spaces in strings

# -> Use stackoverflow to get answer for your errors in program

                              # Excercise - 1

# Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.

# Expected Output:

# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')

# Answer:

print("Day 1 - Python Print Function")
print( "The function is declared like this:")
print("print('what to print')")

#----------------------------------------------------------

                           # String Manipulation

print("Hello World! \nHello world! ") # \n used to print the word 2 times without using print 2 times

# Concatenate

print("Hello" + "Ayyappan") # there is space between hello and ayyappan

# adding space in 3 ways
print("Hello" + " Ayyappan")  # or
print("Hello " + "Ayyappan")  # or
print("Hello" + " " + "Ayyappan") 

                       # Excercise - 2       -> Debug the Code
 
#Fix the code below 👇

# print(Day 1 - String Manipulation")
# print("String Concatenation is done with the "+" sign.")
#   print('e.g. print("Hello " + "world")')
# print(("New lines can be created with a backslash and n.")

# Answer: 

print("Day 1 - String Manipulation")  # " is missing
print('String Concatenation is done with the "+" sign.') # use single quote to avoid error
print('e.g. print("Hello " + "world")') # avoid space at beginning (indentation error)
print("New lines can be created with a backslash and n.") # remove ( at first.

#--------------------------------------------------------------

                        # Python Input Function

print("Hello " + input("What is your name?"))  # getting input from a user

# Comment

# ->  # is used to comment and python will not read the program you enter with #

                             # Excercise -3 

# Write a program that prints the number of characters in a user's name.

# Answer:

print(len("Ayyappan")) # or

print(len(input("What is your name? ")))

#--------------------------------------------------------------

                           # Python Variables

name = input("Enter your nice name here: ")  # here name is a variable
print(name)

name = input("Enter your nice name here: ")
length=len(name)    # length is also a variable
print(length)

#print text in next line \n
name = input("What is your name? ")
age = input("please enter your age: ")
#print(name)
#print(age)

print("Your name is: " + name + "\n" + "Your age is: " + age)

                               # Excercise - 4

# Write a program that switches the values stored in the variables a and b.

# Answer:

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#--------------------------------------------------------------
