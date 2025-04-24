import csv
import os
from collections import Counter
from typing import List, Dict

DATA_FILE = 'YetAnotherMakeupCompany.csv'
OUTPUT_FILE = 'makeup_stats.csv'
PRINT_LIST = 1
HIGHEST_SALES = 2
LOWEST_SALES = 3
CALC_AVERAGE = 4
SAVE_STATS = 5
QUIT = 99

def main():
    
    # Check if the data file exists
    if not os.path.isfile(DATA_FILE):
        print(f'Error: {DATA_FILE} file not found.')
        return
    
    makeup_list = read_csv(DATA_FILE) # initialize makeup list
    makeup_dictionary = {} # initialize makeup dictionary
    
    # Menu Choices
    menu = (
        "Makeup Company Sales Statistics Menu\n"
        "1. Display Sales List\n"
        "2. Calculate and Display Highest Sales\n"
        "3. Calculate and Display Lowest Sales\n"
        "4. Calculate and Display Average Sales\n"
        "5. Save Statistics to File\n"
        "99. Quit"
    )
    
    # Main Loop
    choice = 0
    while choice != QUIT:
        choice = input_menu_choice(menu, [PRINT_LIST, HIGHEST_SALES, LOWEST_SALES, CALC_AVERAGE, SAVE_STATS, QUIT])
        
        if choice == PRINT_LIST:
            print_list(makeup_list)
        elif choice == HIGHEST_SALES:
            value, name = highest_sales(makeup_list)
            print(f'Person with Highest Sale: {name}')
            print(f'Highest Sale: ${value:.2f}')
        elif choice == LOWEST_SALES:
            value, name = lowest_sales(makeup_list)
            print(f'Person with Lowest Sale: {name}')
            print(f'Lowest Sale: ${value:.2f}')
        elif choice == CALC_AVERAGE:
            value = calc_average(makeup_list)
            print(f'Average Sales: ${value:.2f}')
        elif choice == SAVE_STATS:
            save_stats(makeup_list)
        elif choice == QUIT:
            print("Exiting the program.")
            break
    
    pass

def read_csv(file: str) -> List[List[int]]:
    try:
        with open(file, newline='') as f:
            reader = list(csv.reader(f))
            return [[int(trans), str(name), str(date), str(product), int(bulk), float(price), str(location)] for trans, name, date, product, bulk, price, location in reader[1:]]
    except Exception as e:
        print(f'Error reading CSV: {e}')
        return []
    
def input_menu_choice(menu: str, valid_choices: List[int]) -> int:
    while True:
        print('-' * 50)
        print(menu)
        print('-' * 50)
        try:
            choice = int(input('Enter your choice: '))
            if choice in valid_choices:
                return choice
            else:
                print(f'Invalid choice. Please choose from {valid_choices}.')
        except ValueError:
            print('Invalid input. Please enter a number.')           

def print_list(data):
    print(f'{"Transaction":<15} {"Name":<15} {"Date":<15} {"Product":<15} {"Bulk":<10} {"Price":<10} {"Location":<15}')
    for row in data:
        print(f'{row[0]:<15} {row[1]:<15} {row[2]:<15} {row[3]:<15} {row[4]:<10d} {row[5]:<10.2f} {row[6]:<15}')

def highest_sales(data: List[List[int]]) -> float:
    highest = max(data, key=lambda x: x[5])
    return highest[5], highest[1]

def lowest_sales(data: List[List[int]]) -> float:
    lowest = min(data, key=lambda x: x[5])
    return lowest[5], lowest[1]

def calc_average(data: List[List[int]]) -> float:
    total_sales = sum(row[5] for row in data)
    if data:
        total_sales = sum(row[5] for row in data)
        return total_sales / len(data)
    else: 
        return 0

def save_stats(data: List[List[int]]):
    try:
        # Calculate highest, lowest, and average sales
        highest_value, highest_name = highest_sales(data)
        lowest_value, lowest_name = lowest_sales(data)
        average_value = calc_average(data)

        # Open the output file and write the statistics
        with open(OUTPUT_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write headers
            writer.writerow(['Statistic', 'Value', 'Name'])
            
            # Write highest sales
            writer.writerow(['Highest Sale', f'${highest_value:.2f}', highest_name])
            
            # Write lowest sales
            writer.writerow(['Lowest Sale', f'${lowest_value:.2f}', lowest_name])
            
            # Write average sales
            writer.writerow(['Average Sale', f'${average_value:.2f}', 'N/A'])

        print(f'Statistics saved to {OUTPUT_FILE}.')
    except Exception as e:
        print(f'Error saving statistics: {e}')

if __name__ == "__main__":
    main()