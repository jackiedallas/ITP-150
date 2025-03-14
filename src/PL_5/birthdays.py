"""
birthdays.py
@author: Jackie Johnson-Dallas
"""

import csv
import textwrap
import re
from datetime import datetime  # library to format dates

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


def get_valid_name(prompt="Enter a name: "):
    while True:
        user_input = input(prompt).strip()
        if user_input.replace(" ", "").isalpha():
            return user_input
        print("Invalid input, please enter a name with letters only.")


def get_valid_birthday(prompt="Enter birthday: "):
    date_formats = [
        "%m/%d/%Y",  # MM/DD/YYYY
        "%d/%m/%Y",  # DD/MM/YYYY
        "%Y-%m-%d",  # YYYY-MM-DD
        "%B %d, %Y",  # Month DD, YYYY (e.g., December 25, 1990)
        "%b %d, %Y",  # Abbreviated Month DD, YYYY (e.g., Dec 25, 1990)
    ]

    while True:
        user_input = input(prompt).strip()
        for format in date_formats:
            try:
                valid_date = datetime.strptime(user_input, format)
                return valid_date.strftime("%Y-%m-%d")
            except ValueError:
                continue
        print("Invalid date format. Please enter a valid birthday in one of these formats:")
        print("MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD, Month DD, YYYY")


def get_valid_integer(min=1, max=7, prompt="Please enter  your choice from the menu: "):
    while True:
        try:
            choice = int(input(prompt))
            if min <= choice <= max:
                return choice  # Return valid input
            else:
                print(
                    f"Invalid choice. Please enter a number between {min} and {max}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def add_birthday(name, birthday, dictionary):
    dictionary.update({name: birthday})


def print_birthday(name, dictionary):
    if name.lower() in dictionary:
        birth_date = datetime.strptime(dictionary[name.lower()], "%Y-%m-%d")
        formatted_birth_date = birth_date.strftime("%B %d, %Y")
        print(f"\n{name.title()}'s birthday is {formatted_birth_date}.")


while choice != QUIT:
    print("\nFriends and their Birthdays.")
    print('-' * 28)
    print(MENU)

    choice = get_valid_integer()

    if choice == LOOK_UP:
        name = get_valid_name()
        print(birthdays.get(name.lower(), 'Not found.'))
    elif choice == ADD:
        add_birthday(get_valid_name().lower(), get_valid_birthday(), birthdays)
    elif choice == CHANGE:
        check_name = get_valid_name(prompt="Enter the name you want to change: ")
        if check_name in birthdays:
            add_birthday(check_name, get_valid_birthday(), birthdays)
            print(
                f"{check_name.title()}'s new birthday is {birthdays[check_name]}.")
    elif choice == PRINT:
        print_birthday(get_valid_name(prompt="Enter the name you want to print: "), birthdays)
    elif choice == DELETE:
        name = get_valid_name(prompt="Enter the name you want delete: ")
        del birthdays[name]
    elif choice == QUIT:
        print("Thanks for using the birthday program, goodbye!")
        break
