### A programme which prints a random word from a list

import random

def printIntro():
    print("Welcome to this random word generator.")
    print("The programme will require you to input a list of words.")
    print("The programme will then pick a random word from this list,")
    print("and print it out :)")

def create_append_list():
    list_1 = list()

    while True:
        x = input("Please enter a new word or 'N' to exit: ").lower()
        list_1.append(x)
        if x == "n":
            break
    return list_1

def print_list(l_list):
    lengthList = len(l_list) - 1
    y = random.randrange(0,lengthList)
    print(l_list[y])

def main():
    printIntro()
    list_1 = create_append_list()
    print_list(list_1)

main()

input("Press enter to continue: ")
