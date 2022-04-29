# Python Programming
# Day-8


# Simple Function
def great():
  print("Hello World")
  print("Hello Angela Yu")
  print("Hello Ayyappan")
great()

# Function that allows for input
def greatings(name):
  print(f"Hello {name}")
greatings("Ayyappan")


# Positional vs Keyword Arguments

#Positional
def greet(name, location):
  print(f"Hello {name}")
  print(f"Your conformed location is: {location} ")
greet("Ayyappan", "India")

# Keyword Arguments
def greet(name, location):
  print(f"Hello {name}")
  print(f"Your conformed location is: {location} ")

greet(name="Ayyappan", location="India") 
# or
greet(location="India", name="Ayyappan")

#------------------------------------------------------

#Excercise - 1

#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#e.g. Height = 2, Width = 4, Coverage = 5
#number of cans = (2 ✖️ 4) ÷ 5

#Answer: 

# we can use import math module also
# import math
#def paint_calc(height, width , cover):
#    wall= wall = (height * width)/cover
#    num_of_cans = math.ceil(wall)

def paint_calc(height, width , cover):
    wall = (height * width)/cover
    num_of_cans = round(wall)
    print(f"You will need {num_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#------------------------------------------------------------

# Excercise - 2

#Prime numbers are numbers that can only be cleanly divided by itself and 1. https://en.wikipedia.org/wiki/Prime_number
#You need to write a function that checks whether if the number passed into it is a prime number or not.
#e.g. 2 is a prime number because it's only divisible by 1 and 2.
#But 4 is not a prime number because you can divide it by 1, 2 or 4. https://cdn.fs.teachablecdn.com/s0gceS97QD6MP5RUT49H
#Here are the numbers up to 100, prime numbers are highlighted in yellow:
#https://cdn.fs.teachablecdn.com/NZqVclSt2qAe8KhTsUtw

def prime_checker(number):
    is_prime = Truea
    for i in range(2, number-1):
        if number % i ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)

#------------------------------------------------------------

# Final Project of Day-8

# Caesar Cipher

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

#encrypt
def encrypt(plain_text, shift_amount):
    cipher_text = "" 
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

#decrypt
def decrypt(cipher_text, shift_amount):
    plain_text =""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")
      
if direction == "encode":
    encrypt(plain_text = text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount=shift)


# Reduce the code 


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == "decode":
            shift_amount = shift_amount * (-1)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


#------------------------------------------------------------------------------------------------------------------------

#Hard Level

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")


#-----------------------------------------------------------------------------------------------------------------------------
