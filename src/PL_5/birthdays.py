"""
birthdays.py
@author: Jackie Johnson-Dallas
"""

import csv
import textwrap

# constants that represent menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
PRINT = 5
SAVE = 6
QUIT = 7

choice = 0
birthdays = {}  # initializing empty birthday dictionary

MENU = textwrap.dedent(f"""
1. Look up a birthday
2. Add a new birthday
3. Change a birthday
4. Delete a birthday
5. Print a birthday
6. Save a birthday
7. Quit the program
""")

while choice != QUIT:
    print("\nFriends and their Birthdays.")
    print('-' * 28)
    print(MENU)
    
    # Keep prompting until a valid integer is entered
    while True:
        try:
            choice = int(input("\nPlease enter your choice from the menu above: "))
            if 1 <= choice <= 7:  # Ensuring choice is within the valid range
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if choice == LOOK_UP:
        name = input("Enter a friend's name: ")
        print(birthdays.get(name.lower(), 'Not found.'))
    elif choice == ADD:
        name = input("Enter a name: ")
        birthday = input("Enter a birthday: ")
        birthdays.update({name.lower(): birthday})
    
    elif choice == QUIT:
        print("Thanks for using the birthday program, goodbye!")
        break


