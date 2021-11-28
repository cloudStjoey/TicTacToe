### Programme which basically counts and displays the count. ###

def printIntro():
    print("Welcome to this Counting Programme")
    print("Please enter a starting number, ending number and")
    print("how much to increment it by, when prompted")

def get_input():
    print("Please ensure you enter a whole integer number. NO DECIMALS!!!")
    sta_num = int(input("Please enter a starting number: "))
    end_num = int(input("Please enter an ending number: "))
    incr_num = int(input("Please enter a number to increment it by: "))

    return sta_num, end_num, incr_num


def count_func(s_num, end, incr):
    x = range(s_num, end, incr)
    for i in x:
        print(i)
    print("Your sequence has been completed.")
    print("Goodbye")

def main():
    printIntro()
    s_n, e_n, in_cr = get_input()
    count_func(s_n, e_n, in_cr)

main()

input("Press Enter to Exit! ")
