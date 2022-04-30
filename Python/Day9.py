                                      # Python Programming
                                            # Day-9


# Python Dictionaries

program_dictionary = {
  "Bug": "An error in a program htat prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again",
}


# retrieve item from a dictionary
print(program_dictionary["Bug"])

# adding new items to dictionary
program_dictionary["Dict"] = "Hello sir."
print(program_dictionary)

# creat an empty dictionary
empty_dictioanry={}

#wipe an existing dictionary
program_dictionary={}
print(program_dictionary)


# edit an item in dictionary
program_dictionary["Dict"] = "Can you please call me."
print(program_dictionary)

# Loop through a dictionary
for key in program_dictionary:
  print(key)  # gives output of keys
  print(program_dictionary[key]) # output of key values


#------------------------------------------------------------------------------------------------------------------

# Excercise - 1

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)



#------------------------------------------------------------------------------------------------------------------

# Nesting List and Disctionary

# Nesting

capitals = {
    "France": "Paris",    # "Key": "Value"
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
    "France" : ["Paris", "Little", "Dijon"],   
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"], # "key" :list["Values"]
}

# Nesting Dictionary in a Dictionary

travel_log = {
    "France" : {"cities_visited" : ["Paris", "Little", "Dijon"],
                "total_visits" : 12},   
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
                 "total_visits" : 5},
}


# Nesting multiple dictionary in a single list

travel_log = [
    {"Country": "France" ,
     "cities_visited" : ["Paris", "Little", "Dijon"],
     "total_visits" : 12
     },   
    {"country" : "Germany",
     "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits" : 5
     },
]


#-----------------------------------------------------------

# Excercise - 2

travel_log = [
    {"Country": "France" ,
     "cities_visited" : ["Paris", "Little", "Dijon"],
     "total_visits" : 12
     },   
    {"country" : "Germany",
     "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits" : 5
     },
]

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country) 
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

#------------------------------------------------------------------------------------------------------


# Final Project of Day-9

from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()


#---------------------------------------------------------------------------------------------------------------
