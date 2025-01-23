"""
input.py
@author: Jackie Johnson-Dallas
Created January 23, 2025
This script prompts the user to input a name, age and income.
Which represents the string, integer, and float datatypes.
"""

# Get user's name
name = input("What is your name?\n")
age = int(input("What is your age?\n"))
income = float(input("How much money do you want to make annually?\n"))

# print the information
print(f"""
Name: {name}\n
Age: {age}\n
Desired Income: ${income.__format__(',.2f')}
""")
