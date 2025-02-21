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

import textwrap
import re

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

# check if package count entered was valid and start loop
if valid_packages:

    # create loop for total packages to ship
    for i in range(packages):
        print(f"Shipping Report {i+1}")
        package_num_prompt = "Please enter the package number (ex. A1, B2): "
        package_weight_prompt = "Please enter weight for Package: "

        # create loop to validate inputs
        valid_info = False
        while not valid_info:

            # initialize variables
            package_num = None
            package_weight = None

            # validate package number
            while package_num is None:

                try:
                    package_num = input(package_num_prompt)
                    pattern = r"^[A-Za-z]\d*$"
                    if not bool(re.match(pattern, package_num)):
                        print("Package number not valid (ex. A1, B2)")
                        package_num = None
                except ValueError:
                    print("Invalid input! Please enter a string.")

            while package_weight is None:

                try:
                    package_weight = int(input(package_weight_prompt))
                    if package_weight < 0:
                        print("Package weight must be at least 0.")
                        package_weight = None
                except ValueError:
                    print("Invalid input! Please enter an integer.")

            # move to next step if all inputs are valid
            valid_info = True
            if valid_info:

                # use match case for each weight condition
                match package_weight:
                    case w if w >= 0 and w <= 15:
                        shipping_cost = 10.00
                    case w if w >= 16 and w <= 35:
                        shipping_cost = 35.00
                    case w if w >= 36 and w <= 75:
                        shipping_cost = 75.00
                    case w if w > 75:
                        shipping_cost = w * 1.00

                report = textwrap.dedent(f"""
                Shipping Weight: {package_weight.__format__('.1f')}
                Shipping Cost: {shipping_cost.__format__('.1')}
                """)
                print(report)
