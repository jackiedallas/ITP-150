"""
login_name.py
@author: Jackie Johnson-Dallas
This script creates a username by slicing the first letter out of the user's
first, middle, and last name, and concatenating them with a random integer.
It then asks the user to enter a password and validates the password to
ensure that it is at least 8 digits in length, contains at least 1 digit,
lowercase letter, and uppercase letter. Boolean flags are used with while
loops to perform the password validation.
"""

import random
import textwrap

# get user's first, middle, and last name then assign a random int
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")
last_name = input("Enter your last name: ")
id_number = random.randint(0, 100)


# get first letter of each input
first_slice = first_name[0:1]
second_slice = middle_name[0:1]
last_slice = last_name[0:1]

# put together the username
login_name = textwrap.dedent(f"""
{first_slice.lower()}{second_slice.lower()}{last_slice.lower()}{id_number}
""")

print("Your system login name is...")
print(login_name)

# rules for password checker
# It must contain at least 8 characters
# It must contain at least 1 lowercase letter
# It must contain at least 1 uppercase letter
# It must contain at least 1 number

valid = False

while not valid:

    # set conditions for checking password complexity
    valid_length = False
    check_upper = False
    check_lower = False
    check_number = False

    password_conditions = textwrap.dedent("""
    Please enter your password.
    It must contain at least 8 characters.
    It must contain at least 1 uppercase letter.
    It must contain at least 1 lowercase letter.
    It must contain at least 1 number.
    """)

    print(password_conditions)
    password = input("Enter your password now:\n")

    # check length
    if len(password) >= 8:
        valid_length = True
    else:
        valid_length = False

    # check for uppercase
    for char in password:
        if char.isupper():
            check_upper = True
        if char.islower():
            check_lower = True
        if char.isdigit():
            check_number = True

    # check if password is valid
    if valid_length and check_upper and check_lower and check_number:
        print("Password is valid.")
        valid = True
    else:
        print("\nPassword complexity requirements not met.")
        if not valid_length:
            print("Your password length did not meet requirements.")
        if not check_upper:
            print("Your password does not have an uppercase letter.")
        if not check_lower:
            print("Your password does not have a lowercase letter.")
        if not check_number:
            print("Your password does not have a number.")

login_info = textwrap.dedent(f"""
Your login username is: {login_name}
Your password is: {password}
""")

print(login_info)
