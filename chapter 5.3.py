### This programme is a dictionary which stores people and their father and grandfather  - if they have any.

### it will be made of random people

def main():

    important_people = {"Boris Johnson": ["Adolf Hitler", "Josepth Stalin"],
    "Gengis Khan": ["Yesugei Khan", "Barton Baghator"],
    "Minamoto No Yoritomo": ["Minamoto No Yoritomo", "Minamoto No Taneyoshi"],
    "Peter Parker": ["George Stacey", "Ben Parker"],
    "Jesus": ["Had no father", "Imran"]}

    choice = None

    while choice != 0:

        print("""Welcome to Who is Your Daddy Programme.
                This programme displays a select group of people and their fathers and grandfathers.
                You may also add or remove people from the programme
                Now what would you like to do:

                0: Exit the programme
                1: Look up a person's father
                2: Look up a person's grandfather
                3: Add a person and their corresponding father/grandfather
                4: Delete a person
                5: Replace a person
                """)
        choice = int(input("Pick a choice: "))

        if choice == 0:
            print("Thank you for using this dictionary. Goodbye and have a good day!!")

        elif choice == 1:
            print("The persons in the programme are: ")

            for i in important_people.keys():
                print(i, end=", ")

            print("\nNow whose father do you want to look up")

            person = input("Please enter the persons name: ").title()

            if person in important_people:

                print("The name of", person, "'s father is: ", important_people[person][0])

            else:
                print("That person was not recognised. Please add him otherwise pick someone else!")

        elif choice == 2:
            print("The persons in the programme are: ")

            for i in important_people.keys():
                print(i, end=", ")

            print("\nNow whose grandfather do you want to look up")

            person = input("Please enter the persons name: ").title()

            if person in important_people:

                print("The name of", person, "'s grandfather is: ", important_people[person][1])

            else:
                print("That person was not recognised. Please add him otherwise pick someone else!")

        elif choice == 3:

            print("Who do you want to add, remember to add both father and grandfather. Duplicates are not permitted")

            print("So use their full name!!")

            term = input("\nWhose the new person. Remember to leave a space after their forename and surname: ").title()

            if term not in important_people:

                father = input("Whose the father: ").title()

                grandfather = input("Whose the grandfather: ").title()

                important_people[term] = [father, grandfather]

            else:

                print("This person already exists. Try using their full name!!")

        elif choice == 4:

            print("Who do you want to remove from the programme")

            print("The following is a list of the people present: ")

            for i in important_people.keys():
                print(i, end=", ")

            delete_person = input("Now who do you want to delete: ").title()

            if delete_person in important_people:
                del important_people[delete_person]
                print("\nOkay, The person, ", delete_person, "was deleted!!")

            else:
                print("\nSorry I can't do that as  ", delete_person, " does not exist!!!")

        elif choice == 5:

            print("The persons in the programme are: ")

            for i in important_people.keys():
                print(i, end=", ")

            print("\nNow which persons father and grandfather do you want me to redefine.")

            redefine = input("Name the person, remember to use space and their full name ',' separates the person: ").title()

            if redefine in important_people:
                father = input("What is the fathers new name: ").title()
                grandfather = input("What is the grandfather's new name: ").title()

                important_people[redefine] = [father, grandfather]

                print("\nThis ", redefine, " has been redefined")

            else:
                print("\nSorry this person, ", redefine, ", does not exist. maybe add him instead!")

        else:
            print("I'm sorry the choice you selected does not exist. Try again!")







main()

input("Press the enter key to continue!!")
