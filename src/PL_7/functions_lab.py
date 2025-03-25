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
print('Call 2 throws an error because we passed only 2 arguments.')
# water(1, 'Dasani') # comment out after the first run
print('Call 3 does not throw an error, but it is logically incorrect.')
water('Nestle Pure Life', 2.69, 1) # logic error qty of 1 instead of price

print('\nTask 6. Keyword Arguments allow flexibility')
def water_keywords(qty, h2o, price):
    print(f'{qty} {h2o} cost ${price:.2f}')

print('\nCall 1. You must supply params')
# water_keywords() # comment out after first run
print('\nCall 2. Keyword Arguments in the same order as the function def.')
water_keywords(qty=2, h2o='Dasani', price=2.69)
print('\nCall 3. Keyword arguments not in the order of the def.')
water_keywords(h2o='deer park', price=2.69, qty=3)
print('Takeawaay. Using keyword arguments allows us to pass in different order')
print('\nCall 4. Can we leave out an argument using keyword arguments? NO')
# water_keywords(h2o='kirkland', price=3.56) # comment out after running first time
print('\nCall 5. try a mix of positional and keyword arguments')
water_keywords(2, h2o='Acqupanna', price=5.00)