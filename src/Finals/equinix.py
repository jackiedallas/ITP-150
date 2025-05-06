"""
equinix.py
@author: Jackie Johnson-Dallas
@date: 2025-05-06
"""

import csv
import os
from typing import List, Tuple

DATA_FILE = 'eqix.csv'

def main():
    # Check if the data file exists
    if not os.path.isfile(DATA_FILE):
        print(f'Error: {DATA_FILE} file not found.')
        return

    equinix_data = read_csv(DATA_FILE)
    # Ensure there is data to process
    if not equinix_data:
        print("No data found in the file.")
        return

    # Call the print_table function to display the data
    print_table(equinix_data, fixed_width=15)
    
    # Call the find_highest function to find the highest value and its date
    highest_date, highest_value = find_highest(equinix_data)
    print(f"\n{'Highest Price':<25}{'Date':<15}")
    print(f"{highest_value:<25.2f}{highest_date:<15}")
    
    # Call the find_lowest function to find the lowest value and its date
    lowest_date, lowest_value = find_lowest(equinix_data)
    print(f"\n{'Lowest Price':<25}{'Date':<15}")
    print(f"{lowest_value:<25.2f}{lowest_date:<15}")
    
    # Find and print days with high trading volume
    print("\nDays where trading volume exceeded 800,000 trades:")
    high_volume_days = find_high_volume_days(equinix_data, volume_threshold=800000)
    print_table(high_volume_days, fixed_width=15)

# Read the CSV file and parse the data into a dictionary
def read_csv(file: str) -> List[List]:
    """
    Reads the CSV file and returns the data as a two-dimensional list.
    """
    try:
        with open(file, newline='', encoding='utf-8-sig') as datafile:
            reader = csv.reader(datafile)
            data = [row for row in reader]  # Convert the entire CSV into a 2D list
            return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def print_table(data: List[List], fixed_width: int = 15):
    """
    Prints the data in a table format with fixed column widths.
    The first column is aligned to the left, and all other columns are aligned to the right.
    """
    if not data:
        print("No data to display.")
        return

    # Get the headers
    headers = data[0]  # First row contains the headers

    # Print the headers with fixed width
    header_row = " ".join(
        f"{headers[i]:<{fixed_width}}" if i == 0 else f"{headers[i]:>{fixed_width}}"
        for i in range(len(headers))
    )
    print(header_row)
    print("-" * len(header_row))  # Separator line

    # Print each row of data with fixed width
    for row in data[1:]:
        print(" ".join(
            f"{str(row[i]):<{fixed_width}}" if i == 0 else f"{str(row[i]):>{fixed_width}}"
            for i in range(len(row))
        ))
        
# find highest value from highs and the date it occurred then print it
def find_highest(data: List[List]) -> Tuple[str, str]:
    """
    Finds the highest value in the data and returns the date it occurred.
    """
    highest_value = float(data[1][2])
    highest_date = data[1][0]
    for row in data[1:]:
        if float(row[1]) > highest_value:
            highest_value = float(row[1])
            highest_date = row[0]
    return highest_date, highest_value

# find lowest value from lows and the date it occurred then print it
def find_lowest(data: List[List]) -> Tuple[str, str]:
    """
    Finds the lowest value in the 'Low' column and returns the date it occurred.
    """
    lowest_value = float(data[1][3])
    lowest_date = data[1][0]  
    for row in data[1:]:
        if float(row[3]) < lowest_value:  
            lowest_value = float(row[3])
            lowest_date = row[0]
    return lowest_date, lowest_value

def find_high_volume_days(data: List[List], volume_threshold: int = 800000) -> List[List]:
    """
    Finds the days where the trading volume exceeded the given threshold.
    """
    # Get the index of the 'Volume' column 
    volume_index = len(data[0]) - 1
    filtered_data = [data[0]]

    # Get rows where the volume exceeds the threshold
    for row in data[1:]:
        if int(row[volume_index]) > volume_threshold:
            filtered_data.append(row)

    return filtered_data

# Main function to run the script    
if __name__ == "__main__":
    main()
