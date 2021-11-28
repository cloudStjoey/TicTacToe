### Programme which basically prints a word printed backwards. ###

def printIntro():
    print("Welcome to this Backwards Word Programme")
    print("Please enter a word and")
    print("i will show you this word printed backwards")

def get_input():
    print("Please ensure you enter a word. numbers would come out stupid")
    word = str(input("Please enter a word: "))

    return word


def back_ward_word(word):
    x = len(word) - 1
    y = range(x, -1 , -1)
    new_word = ""
    for i in y:
        new_word += word[i]
    print(new_word)


    print("Your backward word has been printed.")
    print("Goodbye")

def main():
    printIntro()
    word = get_input()
    back_ward_word(word)

main()

input("Press Enter to Exit! ")
