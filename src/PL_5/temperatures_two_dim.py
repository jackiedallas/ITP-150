"""
temperatures_two_dim.py
@author Jackie Johnson-Dallas
This script stores information about temperatures recording the dates, 
6 lows, highs, and calculating the average temperature for the date in 
a two dimensional list.
"""
import textwrap

# num_days will set the sizes of the lists
num_days = int(input("How many days do you want to track temperatures? "))
COLS = 4
sum_high_temp = 0
HIGH_TEMP = 60

# initialize the list by datatype and the size via num_days
temperatures = [[0 for col in range(COLS)] for row in range(num_days)]
# print(temperatures)

# loop that loads the values in to the dates, lows, highs columns [0, 1, 2]
# within the temperatures list and calculates the values for the average temps
# column which is column 3
for row in range(0, num_days, 1):
    temperatures[row][0] = input('Please enter the date (ex. Mar. 4): ')
    print(f"Please enter the low for {temperatures[row][0]}:")
    temperatures[row][1] = float(input())
    print(f"Please enter the high temperature for {temperatures[row][0]}:")
    temperatures[row][2] = float(input())
    temperatures[row][3] = (temperatures[row][1] + temperatures[row][2]) / 2
# print(temperatures)
print('-' * 50)

# loop that prints the details more prettily from lists
print(f"{'Dates':10}{'Lows':^12}{'Highs':^12}{'Average Temps':^17}")
for row in range(0, num_days, 1):
    report = f"{temperatures[row][0]:10}{temperatures[row][1]:^12.1f}{temperatures[row][2]:^12.1f}{temperatures[row][3]:^17.1f}"
    print(report)


print('-' * 50)

# algorithm to find the lowest low and it's date
lowest_low = temperatures[0][1]  # use min only with single dimension list
lowest_low_date = temperatures[0][0]

for row in range(0, num_days, 1):
    if temperatures[row][1] < lowest_low:
        lowest_low = temperatures[row][1]
        lowest_low_date = temperatures[row][0]

print(f"{'Lowest Low':30s} {lowest_low:>12.1f}°F")
print(f"{'Lowest Low Date':30s} {lowest_low_date:>12s}")

# algorithm to find the highest high
highest_high = temperatures[0][2]
highest_high_date = temperatures[0][0]

for row in range(0, num_days, 1):
    if temperatures[row][2] > highest_high:
        highest_high = temperatures[row][2]
        highest_high_date = temperatures[row][0]

print(f"{'Highest High':30s} {highest_high:>12.1f}°F")
print(f"{'Highest High Date':30s} {highest_high_date:>12s}")

# code to calculate the average of the highs
for row in range(0, num_days, 1):
    sum_high_temp += temperatures[row][2]

average_highs = sum_high_temp / len(temperatures)

print(f"{'Average Highs':30s} {average_highs:>12.1f}°F")

# algorithm to print based on conditional high temp
for row in range(num_days):
    if temperatures[row][2] >= HIGH_TEMP:
        print(f"The high temp exceeded {HIGH_TEMP}°F on {temperatures[row][0]} -- {temperatures[row][2]}°F.")
print('-' * 50)