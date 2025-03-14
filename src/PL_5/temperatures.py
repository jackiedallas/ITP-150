"""
temperatures.py
@author: Jackie Johnson-Dallas
This script tracks temperatures over a number of days chosen by the user.
"""

# prompt user for days to track
num_of_days = int(input("How many days do you want to track temperatures: "))

# initialize the list specifying data type and size
dates = [' '] * num_of_days
lows = [0.0] * num_of_days
highs = [0.0] * num_of_days
average_temps = [0.0] * num_of_days


# loop that loads data into the lists, the user enters the data except for 
# average_temps and we calculate that.
for i in range(num_of_days):
    dates[i] = input('Please enter the date: ')
    print('Please enter the low for ', [dates[i]])
    lows[i] = float(input())
    print('Please enter the high for ', dates[i])
    highs[i] = float(input())
    average_temps[i] = (lows[i] + highs[i]) / 2

# loop to print each item in the list in a columnar format
print('-' * 51)
print(f'{'Dates':8} {'Lows':>10s} {'Highs':>10s} {'Average Temps':>20s}')
for i in range(len(dates)):
    print(f'{dates[i]:8} {lows[i]:10.1f} {highs[i]:10.1f} {average_temps[i]:20.1f}')
print('-' * 51)

# code block for finding lowest low and the date it occured on
lowest_low = min(lows)
lowest_low_date = ' '
for i in range(len(lows)):
    if lows[i] == lowest_low:
        lowest_low_date = dates[i]
print('-' * 51)
print(f'{'Lowest Low Temp':30} {lowest_low:20,.1f}')
print(f'{'Lowest Low Date':30} {lowest_low_date:>20s}')
print('-' * 51)

# code block for finding highest high temp and the date it occured on
highest_high = max(highs)
highest_high_date = ' '
for i in range(len(highs)):
    if highs[i] == highest_high:
        highest_high_date = dates[i]
        
print('-' * 51)
print(f'{'Highest High Temp':30} {highest_high:20,.1f}')
print(f'{'Highest High Date':30} {highest_high_date:>20s}')
print('-' * 51)

# get the average of the average temps
sum_average_temps = sum(average_temps)
average_of_average_temps = sum_average_temps / len(average_temps)

print('-' * 51)
print(f'{'Average of Average Temps':30} {average_of_average_temps:20,.1f}')
print('-' * 51)
