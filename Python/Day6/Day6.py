                                                                   #Python Programming 
                                                                         # Day-6

# Defining and Calling Python Function

# create or define a function
def my_fucntion(): # def -> keyword, my_function -> function name with paranthesis and colon
  print("Hello World!.")
  print("Bye")

my_fucntion()   # calling the function
# A function is a block of code which only runs when it is called.


# A Simple Robot game

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



