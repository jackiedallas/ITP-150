"""
birthdays.py
@author: Jackie Johnson-Dallas
"""

import csv
import textwrap
from datetime import datetime

# Constants representing menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
PRINT = 5
SAVE = 6
PRINT_ALL = 7
QUIT = 8

choice = 0
birthdays = {}  # Initializing empty birthday dictionary

MENU = textwrap.dedent("""
1. Look up a birthday
2. Add a new birthday
3. Change a birthday
4. Delete a birthday
5. Print a birthday
6. Save birthdays
7. Print all birthdays
8. Quit the program
""")


def get_valid_name(prompt="Enter a name: "):
    """Validates and returns a name with only alphabetical characters and spaces."""
    while True:
        user_input = input(prompt).strip()
        if user_input.replace(" ", "").isalpha():
            return user_input.lower()  # Standardized to lowercase for consistency
        print("Invalid input, please enter a name with letters only.")


def get_valid_birthday(prompt="Enter birthday: "):
    """Validates and returns a properly formatted birthday (YYYY-MM-DD)."""
    date_formats = [
        "%m/%d/%Y",  # MM/DD/YYYY
        "%d/%m/%Y",  # DD/MM/YYYY
        "%Y-%m-%d",  # YYYY-MM-DD
        "%B %d, %Y",  # Month DD, YYYY (e.g., December 25, 1990)
        "%b %d, %Y",  # Abbreviated Month DD, YYYY (e.g., Dec 25, 1990)
    ]

    while True:
        user_input = input(prompt).strip()
        for date_format in date_formats:
            try:
                valid_date = datetime.strptime(user_input, date_format)
                return valid_date.strftime("%Y-%m-%d")  # Store in a standard format
            except ValueError:
                continue
        print("Invalid date format. Please enter a valid birthday in one of these formats:")
        print("MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD, Month DD, YYYY")


def get_valid_integer(min_val=1, max_val=8, prompt="Please enter your choice from the menu: "):
    """Ensures user input is a valid integer within a specified range."""
    while True:
        try:
            choice = int(input(prompt))
            if min_val <= choice <= max_val:
                return choice
            else:
                print(f"Invalid choice. Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def add_birthday(name, birthday, dictionary):
    """Adds or updates a birthday in the dictionary."""
    dictionary[name] = birthday


def format_birthday(birthday):
    """Formats a stored birthday (YYYY-MM-DD) into a readable format (Month DD, YYYY)."""
    birth_date = datetime.strptime(birthday, "%Y-%m-%d")
    return birth_date.strftime("%B %d, %Y")


def print_birthday(name, dictionary):
    """Prints a single birthday in a formatted manner."""
    if name in dictionary:
        formatted_birthday = format_birthday(dictionary[name])
        print(f"\n{name.title()}'s birthday is {formatted_birthday}.")
    else:
        print(f"\n{name.title()} not found in the birthday list.")


def print_all_birthdays(dictionary):
    """Prints all birthdays in the dictionary in a formatted manner."""
    if not dictionary:
        print("No birthdays found.")
        return

    print("\nAll Friends and Their Birthdays:")
    print('-' * 30)
    for name, birthday in dictionary.items():
        print(f"{name.title()}'s birthday is {format_birthday(birthday)}.")


def save_birthdays(dictionary, file_name="birthdays.csv"):
    """Saves the birthday dictionary to a CSV file."""
    try:
        with open(file_name, mode='w', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Birthday"])
            for name, birthday in dictionary.items():
                writer.writerow([name.title(), format_birthday(birthday)])
        print(f"Birthdays saved to {file_name}.")
    except Exception as e:
        print(f"Error saving file: {e}")


while choice != QUIT:
    print("\nFriends and Their Birthdays")
    print('-' * 28)
    print(MENU)

    choice = get_valid_integer()

    if choice == LOOK_UP:
        name = get_valid_name()
        print_birthday(name, birthdays)

    elif choice == ADD:
        name = get_valid_name()
        if name in birthdays:
            print(f"{name.title()} already exists. Use the change option instead.")
        else:
            add_birthday(name, get_valid_birthday(), birthdays)
            print(f"Added {name.title()}'s birthday.")

    elif choice == CHANGE:
        name = get_valid_name(prompt="Enter the name you want to change: ")
        if name in birthdays:
            birthdays[name] = get_valid_birthday()
            print(f"{name.title()}'s new birthday is {format_birthday(birthdays[name])}.")
        else:
            print(f"{name.title()} not found in the birthday list.")

    elif choice == DELETE:
        name = get_valid_name(prompt="Enter the name you want to delete: ")
        if name in birthdays:
            del birthdays[name]
            print(f"{name.title()}'s birthday has been deleted.")
        else:
            print(f"{name.title()} not found in the birthday list.")

    elif choice == PRINT:
        print_birthday(get_valid_name(prompt="Enter the name you want to print: "), birthdays)

    elif choice == SAVE:
        save_birthdays(birthdays)

    elif choice == PRINT_ALL:
        print_all_birthdays(birthdays)

    elif choice == QUIT:
        print("Thanks for using the birthday program, goodbye!")
        break
