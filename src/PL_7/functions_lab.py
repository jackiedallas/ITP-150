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
    pass  # You can put in the keyword pass for an incomplete function


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
water('Nestle Pure Life', 2.69, 1)  # logic error qty of 1 instead of price

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
print('Positional arguments must come before keyword args')
print('\nCall 6. Keyword args can not follow positional arguments')
# water_keywords(qty=2, 'liquid death', price=4.78) # comment out after first run

print('\nTask 7. Default parameters allow us to set defaults values for a\
    parameter in the function definition.')


def water_default(qty=1, h2o='aquafina', price=2.96):
    print(f'{qty} {h2o} ${price:.2f}')


print('\nCall 1. Calling the defaults')
water_default()
print('\nCall 2. Sending different arguments than default')
water_default(2, 'saratoga', 5.00)
print('Takeaway is that if you send different arguments when \
    calling a function with default parameters, your arguments\
        will override the defaults which is a good thing.')
print('\nCall 3. Sending up 2 arguments to see the default come into play')
water_default(2, 'fiji')
print("Takeaway is that you can use positional and keyword arguments")
print("With a function that has default parameters but you still must")
print("follow the rule that positional arguments must come before ")
print("keyword arguments.")

print("\nTask 8. *args (Argument Tuple Packing")
print("You can use argument tuple packing when you don't know how")
print("many arguments you need.")


def args_function(*args):
    print(args)
    print(type(args), len(args))
    for x in args:
        print(x)


args_function(2, 4, 6, 8, 10)

print("\nTask 9. Practical Example of *args")


def avg_args(*args):
    sum_args = 0
    for i in args:
        sum_args = sum_args + i
    return sum_args / len(args)


print(avg_args(2, 4, 6, 8, 10))
print(avg_args(1, 3, 5))

print("\nTask 10. Argument Tuple Unpacking")
print("This works with tuples, lists, and sets. Example is tuple.")


def unpack_args(a, b, c):
    print("a is ", a)
    print("b is ", b)
    print("c is ", c)


stuff = (1, "Perrier", 5.00)
print(type(stuff))
unpack_args(*stuff)

print("\nTask 11. Argument Tuple Packing and Unpacking.")
print("This works with tuples, lists, and sets. Example is a tuple.")


def packing(*args):
    print(type(args), args)


stuff = (1, "Perrier", 5.00)
packing(*stuff)

print('\nTask 12. Arbitrary Keyword Arguments, **kwargs"')
print('If you do not know how many keyword arguments that will be passed into \
your function, add two asterisk: ** before the parameter name in the \
function definition.') 
def pets_function(**pets): 
    print("My dog's name is " + pets["dog"]) 
    print("My cat's name is " + pets["cat"]) 

pets_function(cat = "Miss Kitty", dog = "Buddy")
