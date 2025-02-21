"""
shipping_costs.py
@author: Jackie Johnson-Dallas

Write the program so that it asks the user how many packages the customer
needs to ship and uses the number of packages to control a loop that processes
each package. Validate the number of packages with a loop to ensure that they
are at least 0. For each package, you will need to get the package number and
weight as input. Validate the weight with a loop to ensure that it is at least
0. The shipping cost will be determined by a decision structure
(if elif else, or ifs with compound conditionals). Display the package number,
weight, and shipping cost for each package processed within the loop.
"""

# import textwrap

# store shipping prompt in variable
shipping_prompt = "Please enter the number of packages you want to ship: "


# use flag and loop to check if package input is valid
valid_packages = False
while not valid_packages:
    try:
        # prompt user for input
        packages = int(input(shipping_prompt))
        if packages > 0:
            valid_packages = True
        else:
            print("You must ship at least 1 package.")
    except ValueError:
        print("Invalid input! You must enter an integer.")

if valid_packages:
    print("made it to valid packages.")
