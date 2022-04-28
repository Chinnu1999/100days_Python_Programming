# Hangman Game (randomly choosing a word and user has to guess the word)


# importing the module named random
import random 

# insert ASCII Value
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Insert an hangman logo and print it in first
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    

print(logo)

# creating a word list
word_list = ["ardvark", "baboon", "camel"]


choosen_word = random.choice(word_list) # choosing the word list randomly with the help of random module & assign variable
word_length = len(choosen_word) # instead of using (len(choosen_word)) we created new variable as - word_length
lives=6 # create a variable - 'lives' to keep track no of lives left.

# create an empty list named = display
display=[]

for _ in range(word_length): # calculate the randomly choosed word range
    display += "_"   # if we choose 'apple' then it will display as ["a","p","p","l","e"]
print(f"Guess the word by see the empty boxes: {display}")

# create a  new variable with false value
end_of_game = False

# Now use while loop for the user to guess again and again.
while not end_of_game:

    # user guessing the hangman game words and all the words are converted into lowercase
    guess = input("Guess a letter: ").lower()

    # check whether the letter choosen by the user is present in random choosing word
    #for letter in choosen_word:
    #    if letter == guess:
    #        print("right")
    #    else:
    #        print("wrong")

    #assign position for the user guess @ display with random choosen word

    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = letter
        
    # if lives goes to 0 then the game will be stoped and print you lose.
    if guess not in choosen_word:
        lives =lives - 1
        if lives == 0:
            end_of_game = True
            print("you lose!..")
        
    
    
    # join all element in the list and turn it to a string
    print(f"{''.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!..")
    
    print(stages[lives])
    
print("The randomly choosed word is " + choosen_word)
