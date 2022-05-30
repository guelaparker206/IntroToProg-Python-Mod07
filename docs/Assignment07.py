# Title: Error Handling
# Description:  ValueError function
# ChangeLog: (Who, When, What)
# GuelaP,5.29.2022 Create script
# ------------------------------------------------- #

# Data -------------------------------------- #
random_num = int  # Declares the age variable as an integer

# Processing -------------------------------------- #
while True:
    """
    Ask use for a number
    """
    try:
        random_num = input("Please enter a number: ")  # Asks user to enter their age
        random_num = int(random_num)
        break
    except ValueError:
        print("That is not a valid number, please try again.")
print("You have enter a valid number. Goodbye.")