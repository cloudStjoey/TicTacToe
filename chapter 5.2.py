### A hero attribute programme which displays the attribute of the player ###

#shows the current number of points available
def show_points(points):
    print("The remaining number of points available to spend are: ", points)

def main():

    hero_points = 30 # total number of points

    hero_attribute = {"Strength": 0, "Health": 0, "Wisdom": 0, "Dexterity": 0} # the attributes for the Character

    choice = 1 # to initiate the while statement



    while choice != 0:

        print("""
        Welcome to the Hero Creator programme.
        In this programme you will set the number of points the hero's attributes has.
        The 4 attributes are: Dexterity, Strength, Health, Wisdom.
        You have a total of 30 points to spend on the 4 attributes.
        Spend wisely!!!
        """)

        print(
        """
        Character Creator: Attributes
        0 - Quit program
        1 - Add points
        2 - Remove points
        3 - Current points left
        4 - Attribute and the number of points
        """)

        choice = int(input("Which choice would you like to choose: "))

        if choice == 0:
            print("Thank you playing. Goodbye and have a nice day.")

        elif choice == 1:
            print("""How many points would you like to add.
                        Remember you have a maximum of""", hero_points, """ to spend"""
                        )

            points_to_spend = int(input("How many hero_points: "))
            current_points_left = hero_points - points_to_spend
            if current_points_left >= 0:
                print(""" Which Attribute would you like to choose:
                                    1: Health
                                    2: Dexterity
                                    3: Strength
                                    4: Wisdom
                                    """)

                choice_attribute = int(input("Choose your attribute from 1 - 4: "))

                if choice_attribute == 1:
                    hero_attribute["Health"] = points_to_spend

                    hero_points = current_points_left

                    print("You currently have,", hero_points, " left to spend.")

                elif choice_attribute == 2:
                    hero_attribute["Dexterity"] = points_to_spend

                    hero_points = current_points_left

                    print("You currently have,", hero_points, " left to spend.")

                elif choice_attribute == 3:
                    hero_attribute["Strength"] = points_to_spend

                    hero_points = current_points_left

                    print("You currently have,", hero_points, " left to spend.")

                elif choice_attribute == 4:
                    hero_attribute["Wisdom"] = points_to_spend

                    hero_points = current_points_left

                    print("You currently have,", hero_points, " left to spend.")

                else:
                    print("Your selection was not valid. Try again.")

            else:
                print("The number of points you selected is not valid as you are spending more points than you have.")





        elif choice == 2:
            print("""Which attribute would you like to remove points from
                        1: Health
                        2: Dexterity
                        3: Strength
                        4: Wisdom
            """)

            choice_attr = int(input("Which attribute would you like to remove points from: "))

            if choice_attr == 1:

                print("Health currently has,", hero_attribute["Health"], " points")

                print("How many points do you want to remove. You cannot exceed", hero_attribute["Health"], " points!")

                points_to_remove = int(input("How many points do you want to remove: "))

                new_points = hero_attribute["Health"]

                if points_to_remove <= new_points:

                    hero_attribute["Health"] = hero_attribute["Health"] - points_to_remove
                    hero_points += points_to_remove

                    print("Health now has ", hero_attribute["Health"], " points!")

                else:
                    print("You selected more points than you have available. Try again!!")


            elif choice_attr == 2:

                print("Dexterity currently has,", hero_attribute["Dexterity"], " points")

                print("How many points do you want to remove. You cannot exceed", hero_attribute["Dexterity"], " points!")

                points_to_remove = int(input("How many points do you want to remove: "))

                new_points = hero_attribute["Dexterity"]

                if points_to_remove <= new_points:

                    hero_attribute["Dexterity"] = hero_attribute["Dexterity"] - points_to_remove
                    hero_points += points_to_remove

                    print("Dexterity now has ", hero_attribute["Dexterity"], " points!")

                else:
                    print("You selected more points than you have available. Try again!!")


            elif choice_attr == 3:

                print("Strength currently has,", hero_attribute["Strength"], " points")

                print("How many points do you want to remove. You cannot exceed", hero_attribute["Strength"], " points!")

                points_to_remove = int(input("How many points do you want to remove: "))

                new_points = hero_attribute["Strength"]

                if points_to_remove <= new_points:

                    hero_attribute["Strength"] = hero_attribute["Strength"] - points_to_remove
                    hero_points += points_to_remove

                    print("Strength now has ", hero_attribute["Strength"], " points!")

                else:
                    print("You selected more points than you have available. Try again!!")


            elif choice_attr == 4:

                print("Wisdom currently has,", hero_attribute["Wisdom"], " points")

                print("How many points do you want to remove. You cannot exceed", hero_attribute["Wisdom"], " points!")

                points_to_remove = int(input("How many points do you want to remove: "))

                new_points = hero_attribute["Wisdom"]

                if points_to_remove <= new_points:

                    hero_attribute["Wisdom"] = hero_attribute["Wisdom"] - points_to_remove
                    hero_points += points_to_remove

                    print("Wisdom now has ", hero_attribute["Wisdom"], " points!")

                else:
                    print("You selected more points than you have available. Try again!!")




        elif choice == 3:
            show_points(hero_points)


        elif choice == 4:

            print("Which attribute would you like to check. Use the first letter of the word. The attributes are: Health, Wisdom, Dexterity, Strength.")

            attr = input("Which attribute's points do you want to know: ").lower()

            if attr == "h":
                print("The total number of points the health attribute has is ", hero_attribute["Health"])

            elif attr == "s":
                print("The total number of points the strength attribute has is ", hero_attribute["Strength"])

            elif attr == "w":
                print("The total number of points the wisdom attribute has is ", hero_attribute["Wisdom"])

            elif attr == "d":
                print("The total number of points the dexterity attribute has is ", hero_attribute["Dexterity"])

            else:
                print("The value you have entered was not recognised. Try again!")

        else:
            print("Your choice was not recognised. Try again!")






main()

input("Press any key to continue! ")
