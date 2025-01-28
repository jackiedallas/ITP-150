"""
seconds_converter.py
@author: Jackie Johnson-Dallas
This script will calculate hours, minutes, and seconds of a given number
then display it to the user.
"""

# Get number of seconds from user
# print("\n")
total_seconds = float(input("\nEnter a number of seconds: "))

# Get the number of hours
hours = total_seconds // 3600

# Get the number of remaining minutes
minutes = (total_seconds // 60) % 60

# Get the number of remaining minutes
seconds = total_seconds % 60

# Display the results
print(f"\nHours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}\n")
