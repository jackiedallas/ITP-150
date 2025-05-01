"""
gas_file_solution.py
@author: Jackie Johnson-Dallas
@date: 2023-10-01
@description: This script reads a gas file, processes the data, and generates a summary report.
"""

import csv

DATA_FILE = 'gas_prices.csv'
OUTPUT_FILE = 'GasStatistics.txt'

def main():
    
    # Process the Data file
    data = process_data(DATA_FILE)
    
    # Display the data
    show_data(data)
    
    # print highs and lows for 2023
    print("\nGas Prices 2023")
    print('-' * 64)
    
    # Get the highest gas price
    highest_price = get_highest_price(data)
    print(f'\nHighest gas price: ${highest_price[0].__format__(".2f")}')
    print(f'Highest month: {highest_price[1]}')
    
    # Get the lowest gas price
    lowest_price = get_lowest_price(data)
    print(f'\nLowest gas price: ${lowest_price[0].__format__(".2f")}')
    print(f'Lowest month: {lowest_price[1]}')
    
    # get the average gas price
    # average_price = get_average_price(data).__format__(".2f")
    
    print(f'\nAverage gas price: ${get_average_price(data)}\n')
    
    print(f'Change in gas price from January 2019 to October 2023: {change_in_percent(data).__format__(".2f")}%\n')
    
    # Save the processed data to a new text file
    save_stats(OUTPUT_FILE, data)

def process_data(data):
    try:
        
        # Read the gas file
        with open(DATA_FILE, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            data = [row for row in reader]

        # Process the data
        for row in range(1, len(data)):
            data[row][1] = float(data[row][1])
            data[row][2] = float(data[row][2])
            data[row][3] = float(data[row][3])
            data[row][4] = float(data[row][4])
            data[row][5] = float(data[row][5])
        
        # Return the processed data
        print("\nData processed successfully.")
        return data
    
    except IOError as ierr:
        print(f'An error occurred while reading the file: {ierr}')
    except IndexError as xerr:
        print(f'An index error occurred: {xerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')

def get_highest_price(data):
    """
    Returns the highest gas price from the data.
    """
    highest_price = data[1][5]
    highest_month = data[1][0]
    for row in range(1, len(data), 1):
        if data[row][5] > highest_price:
            highest_price = data[row][5]
            highest_month = data[row][0]
    return highest_price, highest_month

def get_lowest_price(data):
    """
    Returns the lowest gas price from the data.
    """
    lowest_price = data[1][5]
    lowest_month = data[1][0]
    for row in range(1, len(data), 1):
        if data[row][5] < lowest_price:
            lowest_price = data[row][5]
            lowest_month = data[row][0]
    return lowest_price, lowest_month

def get_average_price(data):
    """
    Returns the average gas price from the data.
    """
    total_price = 0
    for row in range(1, len(data)):
        total_price += data[row][5]
    average_price = total_price / (len(data) - 1)
    return average_price
    

def save_stats(file_path, data):
    """
    Saves the processed data to a new CSV file.
    """
    try:
        output_file = open(file_path, 'w')
        output_file.write(f'{"Lowest Month":<30s}{get_lowest_price(data)[1]:>15s}{"\n"}')
        output_file.write(f'{"Lowest Price":<30s}{get_lowest_price(data)[0]:>15.2f}{"\n"}')
        output_file.write(f'{"Highest Month":<30s}{get_highest_price(data)[1]:>15s}{"\n"}')
        output_file.write(f'{"Highest Price":<30s}{get_highest_price(data)[0]:>15.2f}{"\n"}')
        output_file.write(f'{"Average Price 2023":<30s}{get_average_price(data):>15.3f}{"\n"}')
        output_file.write(f'{"Percent +/-":<30s}{change_in_percent(data):>15.3f}')
        print(f'\nData saved to {file_path} successfully.')
    except IOError as ierr:
        print(f'An error occurred while writing to the file: {ierr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')

def show_data(data):
    """
    Displays the processed data.
    """
    
    print("\nList of Gas Prices 2019-2023")
    print('-' * 64)
    
    data_to_print = f"{data[0][0]:10}{data[0][1]:>10s}{data[0][2]:>10s}{data[0][3]:>10s}{data[0][4]:>10s}{data[0][5]:>10s}"
    print(data_to_print)
    
    for row in range(1, len(data)):
        gas_prices = f"{data[row][0]:10}{data[row][1]:>10.2f}{data[row][2]:>10.2f}{data[row][3]:>10.2f}{data[row][4]:>10.2f}{data[row][5]:>10.2f}"
        print(gas_prices)

def change_in_percent(data):
    change = data[12][5] - data[1][5]
    percent = change / data[1][5] * 100
    return percent      

if __name__ == "__main__":
    main()