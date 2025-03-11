"""
cups_to_gallons_debug.py
@author PUT YOUR NAME HERE
@version 1
@see

Requirements:
   
This program changes cups into gallons.
It can only compute measurements for cups that are entered as a whole number.
Also, a valid amount of cups must divide evenly by 16 with no remainder.
FYI the if statement for detecting a multiple of 16
for a variable named cups is
if cups % 16 == 0:

The user gets 3 attempts at entering a value in cups 
that will divide evenly by 16 into gallons.
If the user enters a valid  amount, then the
program displays the quantity of gallons and
breaks out of the loop as shown in the test cases
below where 32 cups is used as the amount to convert into gallons:
   
How to test for a valid amount:
This program will convert cups into gallons for a given amount of cups.
You are allowed 3 tries to enter an amount evenly divisible by 16.
Attempt 1: Please enter cups to change into gallons:
As an example, for 32 cups, enter 32.
32
32 cups converts to 2 gallons! 
Thanks for converting cups to gallons.


How to test for invalid amounts. Notice in the
following test case, the user makes 2 attempts which
are invalid (39, 33) before entering a valid
amount on the 3rd try which is 16.

This program will convert cups into gallons for a given amount of cups.
You are allowed 3 tries to enter an amount evenly divisible by 16
Attempt 1: Please enter cups to change into gallons:
As an example, for 32 cups, enter 32.
39
Invalid. 2 more attempt(s)!
39 cups will not divide evenly into gallons.
Attempt 2: Please enter cups to change into gallons:
As an example, for 32 cups, enter 32.
33
Invalid. 1 more attempt(s)!
   
33 cups will not divide evenly into gallons.
Attempt 3: Please enter cups to change into gallons:
As an example, for 32 cups, enter 32.
16
16 cups converts to 1 gallons! 
Thanks for converting cups to gallons.
Notice that you must keep track of invalid attempts and
let the user know how many attempts that they have
left before using up all attempts.

"""


tries = 3
counter = 1

print("This program will convert cups into gallons for a given amount of cups.")
print("You are allowed 3 tries to enter an amount evenly divisible by 16")

while counter <= tries:

    print(f"Attempt {counter}: Please enter cups to change into gallons:")
    print("As an example, for 32 cups, enter 32.")
    cups = int(input())
    if cups % 16 == 0:
        gallons = cups / 16
        print(f"{str(cups)} cups converts to {gallons.__format__('.1f')} gallons!")
        break
    else:
        print(f"Invalid. {tries-counter} more attempt(s)!")
    print(str(cups) + " cups will not divide evenly into gallons.\n")
    counter += 1

    print("Thanks for converting cups to gallons.")
