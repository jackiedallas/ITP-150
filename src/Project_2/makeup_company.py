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
    # print(makeup_list)
    
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
            display_list(makeup_list)
        elif choice == HIGHEST_SALES:
            highest_sales = calc_highest_sales(makeup_list)
            print(f'Highest Sales: {highest_sales}')
        elif choice == LOWEST_SALES:
            lowest_sales = calc_lowest_sales(makeup_list)
            print(f'Lowest Sales: {lowest_sales}')
        elif choice == CALC_AVERAGE:
            average_sales = calc_average_sales(makeup_list)
            print(f'Average Sales: {average_sales}')
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

if __name__ == "__main__":
    main()