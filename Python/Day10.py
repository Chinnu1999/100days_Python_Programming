                              # Python Programming
                             # Day-10

# Functions with output

def format_name(f_name, l_name):
    print(f_name.title())
    print(l_name.title())
format_name("angela", "ANGELA")

#-----------------------------------------

def format_name(f_name, l_name):
    formated_f_name =  f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")
format_name("Ayyappan","A")

#-----------------------------------------

def format_name(f_name, l_name):
    formated_f_name =  f_name.title()
    formated_l_name = l_name.title()
    return (f"{formated_f_name} {formated_l_name}")
formated_string = format_name("Ayyappan","A")
print(formated_string)

#-----------------------------------------

# Multiple return function

def format_name(f_name, l_name):
    if f_name == "" or l_name=="":
        return "Please enter your name"
    formated_f_name =  f_name.title()
    formated_l_name = l_name.title()
    return (f" Return: {formated_f_name} {formated_l_name}")
print(format_name(input("What is your first name?"), input("What is your last name? ")))

#---------------------------------------------

# Excercise - 1

# In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False if it is not a leap year.

# You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

#days_in_month(year=2022, month=2)
#And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

#28
#The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

# Answer:



def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False
    
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > 12 or month < 1:
    return "Invalid month entered."
  if month == 2 and is_leap(year):
    return 29
  return month_days[month - 1]
   
#Do NOT change any of the code below 👇
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# Docstrings (used for multi-line comments)

def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case
    version of the name."""    
    if f_name == "" or l_name=="":
        return "Please enter your name"
    formated_f_name =  f_name.title()
    formated_l_name = l_name.title()
    return (f" Return: {formated_f_name} {formated_l_name}")
print(format_name(input("What is your first name?"), input("What is your last name? ")))

#-------------------------------------------------------------------------------------------

# Calculator Program

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()


#--------------------------------------------------------------------------------------------------------------------------------------------------
