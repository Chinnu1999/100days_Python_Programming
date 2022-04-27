                                                                   #Python Programming 
                                                                         # Day-6

# Defining and Calling Python Function

# create or define a function
def my_fucntion(): # def -> keyword, my_function -> function name with paranthesis and colon
  print("Hello World!.")
  print("Bye")

my_fucntion()   # calling the function
# A function is a block of code which only runs when it is called.


# A Simple Robot game - https://reeborg.ca/index_en.html

def turn_right():   # instead of using turn left 3 times we use function as turn right()
    turn_left()
    turn_left()
    turn_left()

turn_left()     # turn robot left
move()          # move forward  
turn_right()    # turn left 3 times
move()
turn_right()
move()
turn_right()
move()
turn_left()
turn_left()

#-------------------------------------------------------------------------------------------------------------------------------------

# Excercise - 1 Hurdle Game

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moving():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

moving()
moving()
moving()
moving()
moving()
moving()


                             # or

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moving():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for i in range(6):
  moving()
  
#---------------------------------------------------------------------------------------
# Indentation in Python

def my_function():
  print("Hello World")   # indented
  print("Hello Earth")   # indented

  
def my_function1():
  print("Hello World") 
print("Hello Earth")     # not indented
# use tab to Indentate

# while Loop

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moving():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hurdles = 6
while number_of_hurdles > 0:
  moving()
  number_of_hurdles = number_of_hurdles - 1
  print(number_of_hurdles)


#-----Excercise 2-------------------------------------------------------------------

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def moving():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    moving()

#---------------------------------------------------------------------------------

#Excercise - 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        

#-------------------------------------------------------------------------------------------------------------------------------

# Excercise - 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

#---------------------------------------------------------------------------------------------------------------------------



