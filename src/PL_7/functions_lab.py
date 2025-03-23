"""
functions_lab.py
@author: Jackie Johnson-Dallas
"""

import random

print('\nTask 1. Import a function.')
integer = random.randint(0, 100)
print(f'A random integer between 1 and 100 is {integer}.')

print('\nTask 2. See the help.')
print("If you want to see a function's documentation, enter help followed by the function name.")
# help(random) # comment this out after running it the first time

print('\nTask 3. Basic function without parameters and arguments.')
def basic_function():
    location = 'We are inside my basic function.'
    print(location)

print('Before calling basic_function.')
basic_function()
print('After calling basic_function.')