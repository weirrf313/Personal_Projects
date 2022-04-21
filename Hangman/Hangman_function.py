# Function to check the users guess ie what letter they have selected
def check_guess(guess, word):
    if guess.lower() in word:
        return 1
    else:
        return 0

# Function to see if they have completed the word
def complete_check(usersguess, word, list):
    list = []
    for letter in usersguess:
        if letter in word:
            list.append(letter)

    if len(set(list)) == len(set(word)):
        return 1
    else:
        return 0

# A function to print out the instruction. Used function to easily change if needed
def print_instructions():
    print("ToDo - Mention that they must only use letters if they enter numbers / special characters it will be accepted and they will lose a life")

