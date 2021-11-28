### Programme which basically jumbles a word and the user has
### to unjumble and guess the word. In this modified version, a hint is available

import random

def printIntro():
    print("Welcome to this Word Jumble Game")
    print("You will see a jumbled word and will have")
    print("to guess what the correct word is. If you get stuck")
    print("then there is a hint available. But be warned, using a hint")
    print("lowers your finally score.\n\n\n")

def word_jumble_generator():
    words_hint = (("python", "Type of Snake"), ("jumble", "an untidy collection of words or things"),
    ("easy", "Opposite of difficult"), ("difficult", "Opposite of Easy"), ("answer", "a solution to a problem"),
    ("xylophone", "a musical instrument that begins with an X"))

    x_random = random.randint(0,5) # generate a random number to select a list at random.

    new_word_hint = words_hint[x_random]

    the_word = new_word_hint[0]
    the_hint = new_word_hint[1]

    ### next jumbling the words

    len_word = len(the_word)
    l = [i for i in range(len_word)]
    random.shuffle(l)

    jumble_word = ""

    for i in l:
        jumble_word += the_word[i]


    return the_word, the_hint, jumble_word

#next print the jumbled word and create a scores

def show_score(jumble_word):

    print("\n\nThe jumbled word is ", jumble_word, "\n")
    score = len(jumble_word) * 5

    return score

#next determining whether player has used a hint and printing their score

def score_print(count, score):

    if count != 0:
        print("Your Score is ", score, "\nWell Done")
    else:
        print("So sorry your score is", score*0.5, "\nbecause you used a hint :(")


#now getting the user to guess the word and if they have used a hint





def main():
    printIntro()
    the_word, the_hint, jumble_word = word_jumble_generator()

    score = show_score(jumble_word)

    count = 1
    guess = input("\nYour guess: ")
    while guess != the_word and guess != "":
        print("Sorry, that is not correct\n")
        x = input("Would you like to use a hint, Y for yes anything else for no: ")
        if x.lower() == "y":
            print(the_hint)
            count = 0

        guess = input("\nYour guess: ")

    if guess == the_word:
        score_print(count,score)


main()


print("Thanks for playing.")
input("Press Enter to Exit! ")
