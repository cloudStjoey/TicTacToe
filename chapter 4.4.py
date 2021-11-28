### programme where the computer picks a random word and gives the player
### 5 guesses to guess the word. The computer can only respond with Yes or No and prints the number
### of letters the word has. Then the player has to guess the word.

import random

def printIntro():
    print("Welcome to this Word Guess Game")
    print("The computer will tell you the number of letters in the word")
    print("You will get 5 chances to ask whether a letter is in the word")
    print("The computer can only respond by saying yes or no")
    print("After five guesses, you must guess the word.\n\n\n")

def word_list_guesser():

    words = ("hangman", "challenge", "japan", "history", "market",
    "bicycle", "gold", "chocolate")

    x_random = random.randint(0,7) # generate a random number to select a list at random.

    new_word = words[x_random]
    split_word = list(new_word)
    ### next get the length of the word

    len_word = len(new_word)
    display_word = "_ "*len_word

    return new_word, split_word, len_word, display_word

def main():
    printIntro()

    new_word, split_word, len_word, display_word = word_list_guesser()

    score = 5*len_word*2.5

    print("The hidden word has ", len_word, " letters. \nGood Luck")
    print(display_word)

    count = 0

    while count != 5:
        guess_letter = input("Please enter your guess: ").lower()
        if guess_letter in split_word:
            print("Yes this letter, ", guess_letter, ", is in the hidden word")
        else:
            print("Sorry this letter, ", guess_letter, ", is not in the hidden word")
        count += 1

    final_guess = input("Now Make your final guess: ").lower()

    if final_guess == new_word:
        print("You got it, the word was ", new_word, " well done!")
        print("Your score is ", score)
    else:
        print("Sorry you too stupid. Better luck next time ;)")
        print("Your Score is 0!!!")

main()

print("Thanks for playing.")
input("Press Enter to Exit! ")
