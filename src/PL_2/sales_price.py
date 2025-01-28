"""
sale_price.py
@author: Jackie Johnson-Dallas
Date Created: January 28th, 2025
This script prompts the user to input a regular price and a discount percent.
It then calculate the discount amount, and sale price and displays a receipt
showing the regular price, discount amount, and sale price.
"""

regular_price = float(input("Please enter the regular price: "))
discount_percent = float(input("Discount percent (ex. 10 for 10%): "))

discount_amount = regular_price * discount_percent / 100
sale_price = regular_price - discount_amount
print(f"\nRegular price: {regular_price.__format__(',.2f')}")
print(f"Discount Amount: {discount_amount.__format__(',.2f')}")
print(f"Sale Price: {sale_price.__format__(',.2f')}")
