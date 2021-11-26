# Python Ptogramming - Day 5

print("Hello Chinnu!")

#---------------------------------------------------------------------------------------------

# For loop

fruits = ['Apple', 'Mango', 'Banana']
print(fruits)

for fruit in fruits:        # creating for loop
  print(fruit)              # print the items one by one
  print(fruit + " Pie")

#---------------------Excercise---------------------------------

# Find height and average of the student

student_height = input("Input a list of student: ").split()  # split used to create a list (input from user)   - [111, 121, 131, 141, 151]
for n in range(0, len(student_height)):                      # here for loop used, range(0 and length of student_height) where (0,5)
  student_height[n] = int(student_height[n])                 # convert to integer (one by one)
print(student_height)                                        # printing student_height [111, 121, 131, 141, 151]


total_height = 0                                             # assign total_height = 0
for height in student_height:                                # student_height = [111, 121, 131, 141, 151]
  total_height = total_height + height                       # adding one by one - 
''' 
                                             totally = 5    total_height = 0 + 111 = 111
                                                            total_height = 111 + 121 = 232
                                                            total_height = 232 + 131 = 363
                                                            total_height = 363 + 141 = 504
                                                            total_height = 504 + 151 = 655

'''
print(total_height)                                          # print the output = 655

total_student = 0                                            # assign total_student = 0
for student in student_height:                               # student_height = [111, 121, 131, 141, 151
  total_student = total_student + 1                          # adding one by one - 
''' 
                                             totally = 5    total_student = 0 + 1 = 1
                                                            total_student = 1 + 1 = 2
                                                            total_student = 2 + 1 = 3
                                                            total_student = 3 + 1 = 4
                                                            total_student = 4 + 5 = 5

'''
print(total_student)                                        # print the output = 5

average = round(total_height / total_student)               # 655 / 5 = 131
print(average)



'''
total_height = sum(student_height)
number_of_student = len(student_height)
average_height = total_height / number_of_student
print(average_height)
'''

#---------------------------------------Excercise 2 ------------------------------------------------------------

# Find the heighest score

student_score = input("Input a list of student score: ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)


highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(highest_score)

# --------------------Lowest score------------------------- 
''''
lowest_score = student_score[0]
for score in student_score:
    if score < lowest_score:
        lowest_score = score
print(lowest_score)

'''
#--------------------------------------------------------------------------------------

# For loop with range

for num in range(0, 10):
    print(num)

for num1 in range(0, 11, 2):   # the output will printed by 0 2 4 6 8 10, here 2 defines the step size
  print(num1) 

# adding numbers from 1 to 100
total = 0
for number in range(0, 101):
    total = total + number
print(total)

#-------------------------------------Excercise 1-----------------------------------------------------------

#adding even numbers from 0 to 100
total = 0
for number in range(0, 101, 2):
    total = total + number
print(total)

                              # or

total1 = 0
for number in range(0, 101):
    if number %2==0:
        total1 = total1 + number
print(total1)


#------------------------------------Excercise 2---------------------------------------------------------

#FizzBuzz

total = 0
for number in range(0,101):
    if number %3 ==0 and number %5 ==0:
        print("FizzBuzz")
    elif number %3 == 0:
        print("Fizz")
    elif number %5 == 0:
        print("Buzz")
    else:
        print(number)

#-------------------------------------------------------------------------------------------------------


