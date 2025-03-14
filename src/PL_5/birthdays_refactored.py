"""
birthdays.py
@author: Jackie Johnson-Dallas
"""

import csv
from datetime import datetime

# Constants representing menu choices
LOOK_UP, ADD, CHANGE, DELETE, PRINT, SAVE, PRINT_ALL, QUIT = range(1, 9)

# Load existing birthdays at startup
def load_birthdays(file="birthdays_refactored.csv"):
    """Loads birthdays from a CSV file, skipping the header."""
    try:
        with open(file, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # ✅ Skip the header row
            return {row[0].lower(): datetime.strptime(row[1], "%B %d, %Y").strftime("%Y-%m-%d")
                    for row in reader if len(row) == 2}  # ✅ Ensure valid rows
    except FileNotFoundError:
        return {}

# Save birthdays to file
def save_birthdays(birthdays, file="birthdays_refactored.csv"):
    """Saves the birthday dictionary to a CSV file."""
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Birthday"])  # ✅ Ensure header is added
        writer.writerows([[name.title(), datetime.strptime(bd, "%Y-%m-%d").strftime("%B %d, %Y")]
                        for name, bd in birthdays.items()])
    print(f"Birthdays saved to {file}.")

# Get valid input functions
def get_valid_name(prompt="Enter a name: "):
    """Ensures name input contains only letters and spaces."""
    while True:
        name = input(prompt).strip()
        if name.replace(" ", "").isalpha():
            return name.lower()
        print("Invalid input, use letters only.")

def get_valid_birthday(prompt="Enter birthday: "):
    """Ensures valid birthday input in multiple formats."""
    date_formats = ["%m/%d/%Y", "%d/%m/%Y", "%Y-%m-%d", "%B %d, %Y", "%b %d, %Y"]
    while True:
        date_str = input(prompt).strip()
        for fmt in date_formats:
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        print("Invalid date format. Use MM/DD/YYYY, DD/MM/YYYY, YYYY-MM-DD, Month DD, YYYY")

# Print functions
def print_birthday(name, birthdays):
    """Prints a single birthday."""
    if name in birthdays:
        print(f"{name.title()}'s birthday is {datetime.strptime(birthdays[name], '%Y-%m-%d').strftime('%B %d, %Y')}.")
    else:
        print(f"{name.title()} not found.")

def print_all_birthdays(birthdays):
    """Prints all stored birthdays."""
    if birthdays:
        for name, bd in birthdays.items():
            print(f"{name.title()}'s birthday is {datetime.strptime(bd, '%Y-%m-%d').strftime('%B %d, %Y')}.")
    else:
        print("No birthdays found.")

# Main program
birthdays = load_birthdays()
print("\n🎉 Welcome to the Birthday Manager! 🎉")
print("Keep track of your friends' birthdays with ease.\n")
while (choice := input("\n1) Look Up  2) Add  3) Change  4) Delete  5) Print  6) Save  7) Print All  8) Quit\nChoice: ").strip()) != "8":
    match choice:
        case "1": print_birthday(get_valid_name(), birthdays)
        case "2": birthdays.setdefault(get_valid_name(), get_valid_birthday())
        case "3": birthdays.update({get_valid_name(): get_valid_birthday()})
        case "4": birthdays.pop(get_valid_name(), print("Name not found."))
        case "5": print_birthday(get_valid_name(), birthdays)
        case "6": save_birthdays(birthdays)
        case "7": print_all_birthdays(birthdays)

print("\nAuto-saving before exit...")
save_birthdays(birthdays)
print("Thanks for using the birthday program, goodbye!")
