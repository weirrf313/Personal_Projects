##############################################################################################
                            ## HANGMAN - PYTHON PROJECT ##
##############################################################################################


# ToDo list/ steps #
####################
# Create username section to keep socore of Easy/Medium/Hard
# Get their score
# Get user input to see which difficulty level they want
'''
    Easy = <= 5 letters
    Medium = > 5 <= 7
    Hard = >= 8 Letters
'''
# SQL Managment to store list of words use randint to gets index of word
# Update users score



##############################################################################################

word = "ruaridh" # Later on look to inport list of words and possible have user select the amount of letter
lives = int(input("How many lives would you like to start with? ")) # This has to be an int so can practice error handaling to ensure they enter a number
usersguess = [] # Empty list used for determing all letters guessed
complete_list = [] # Empty list to use in function to account for words with two or more of the same letters in it

from Hangman_function import check_guess, complete_check

# Start of the While loop (aka the game) making sure lives are above 0 and that if they get it wrong they lose a life.
while lives > 0:
     # For loop to go over the word
    for letter in word:
        # If a letter in the word is in the user guess then print else print _ for viz
        if letter.lower() in usersguess:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print("")
    
    prompt = "Next Guess: "
    guess = input(prompt)
        
    if check_guess(guess, word):
        usersguess.append(guess.lower())
    else:
        lives -= 1
        print("Incorrect")
    
    if complete_check(usersguess, word, complete_list):
        print("Congratulations you solved the word!\nThe word was: %s" %(word))
        break







