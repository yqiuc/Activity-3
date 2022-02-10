def display_title():
    # Displays the title of the program when called.
    print("Welcome to the Grade Calculator")
    print()

def get_totalpoints():
    total_points = int(input("Enter the total score (0 - 1000):"))
    while (not(total_points >= 0 and total_points <= 1000)):
        print("You must enter integer values >= 0 and <= 1000. Try again.")
        print()
        total_points = int(input("Enter the total score (0 - 1000):"))
    return total_points

# calculate lettergrade
def get_lettergrade(averageEarned):
    if (averageEarned >= 92 and averageEarned <= 100):
        return 'A'
    elif (averageEarned >= 88 and averageEarned <= 91.99):
        return 'B+'
    elif (averageEarned >= 82 and averageEarned <= 87.99):
        return 'B'
    elif (averageEarned >= 78 and averageEarned <= 81.99):
        return 'C+'
    elif (averageEarned >= 70 and averageEarned <= 77.99):
        return 'C'
    elif (averageEarned >= 60 and averageEarned <= 69.99):
        return 'D'
    elif (averageEarned < 60):
        return 'F'

def main():
    display_title()
    choice = 'y'
    while(choice == 'y'):
        # get input from the user.
        total_points = get_totalpoints()
        # calculate average
        average = total_points / 1000 * 100
        letter_grade = get_lettergrade(average)
        print("You earned an average of: {}%.".format(average), "Letter grade earned:", letter_grade)
        print()

        # see if the user wants to continue.
        choice = input("Would you like to enter another score (y/n)?")
        print()

if __name__ == "__main__":
    main()