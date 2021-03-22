import sys

#how many lives we have
no_of_tries = 5

#word which we will be guessing
word = "dominika"

#list with letters which user used
used_letters = []

#list with letters from user
user_word = []


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if  letter == letter_in_word:
            indexes.append(index)  
    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print("Number of tries", no_of_tries)
    print("Used letters: ", used_letters)
    print()
    
#list initialization
for _ in word:
    user_word.append("_")
    
#asking about letter
while True:
    letter = input("Enter the letter: ")
    used_letters.append(letter)
    
    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("There is no such letter")
        no_of_tries -= 1
        

        if no_of_tries == 0:
            print("End of game :(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("You won!")
            sys.exit(0)

        show_state_of_game()


