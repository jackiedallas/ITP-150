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
    print("Friends and their Birthdays.")
    print('-' * 28)
    print(MENU)
    choice = int(input("\nPlease enter your choice from the menu above:\n"))
    
    while choice < 1 or choice > 7:
        choice = int(input("Invalid. Please enter a choice from 1 to 7:\n"))

