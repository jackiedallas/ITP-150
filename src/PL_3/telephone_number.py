"""
telephone_number.py
@author: Jackie Johnson-Dallas
"""

from operator import itemgetter

# CONSTANTS are in ALL CAPS.
FORMATTED_LENGTH = 13
UNFORMATTED_LENGTH = 10

valid = True  # Flag to indicate a valid format
telephone = input("""
Please enter the telephone number in this format (xxx)xxx-xxxx: """)

# store indices and chars to match in tuples
indices = (0, 4, 8)
special_chars = ('(', ')', '-')
results = itemgetter(*indices)(telephone) == special_chars

if results:
    valid = True
    print(f"Great! Telephone number: {
        telephone} is a properly formatted number.")
    # print(telephone)
else:
    valid = False
    print(f"Yikes, this phone number: {telephone} is not properly formatted.")
    # print(telephone)

# accept telephone as correct format and return as incorrect format
if valid:
    # the first number is inclusive, the second number is exclusive
    area_code = telephone[1: 4:]
    three_digit_prefix = telephone[5: 8:]
    line_number = telephone[9: 13:]
    unformatted_number = area_code + three_digit_prefix + line_number
    print(f"Telephone number input is now unformatted as: {
        unformatted_number}")
else:
    area_code = telephone[0: 3:]
    three_digit_prefix = telephone[3: 6:]
    line_number = telephone[6: 10:]
    formatted_number = f'({area_code}){three_digit_prefix}-{line_number}'
    print(f"The phone number input is now formatted as {formatted_number}")
