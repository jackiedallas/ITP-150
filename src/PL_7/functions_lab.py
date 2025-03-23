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

print('\nTask 4. Basic function that has a docstring & the keyword pass.')
def empty_function():
    """This function is empty but has this line of documentation."""
    pass # You can put in the keyword pass for an incomplete function
empty_function()
# help(empty_function)

print('\nTask 5. Positional Arguments require same qty of arguments and \
    parameters in the same order representing the same data types.')
def water(qty, h2o, price):
    print(f'{qty} {h2o} cost ${price:.2f}')
print('Call 1:')
water(1, 'Smart Water', 2.69)
