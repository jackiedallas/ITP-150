"""
guido_says.py
@author: Jackie Johnson-Dallas
"""

welcome_message = "Let's play Guido Says!"
guido_says = "Guido Says... "
print(welcome_message)
name = input("Please enter a first, middle, and last name: ")


print(f"{guido_says} split at the space: {name.split()}")
print(f"{guido_says} reverse the name: {name[::-1]}")
print(f"{guido_says} make the name lowercase: {name.lower()}")
print(f"{guido_says} make the name UPPERCASE: {name.upper()}")
print(f"{guido_says} make the name Title Case: {name.title()}")
print(f"{guido_says} find the length of the name: {len(name)}")
