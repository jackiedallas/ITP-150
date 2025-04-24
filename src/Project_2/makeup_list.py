import csv
import os
from collections import Counter
from typing import List, Dict, Tuple

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
    
    makeup_data = read_csv(DATA_FILE)  # Initialize makeup data as a dictionary
    
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
            print_list(makeup_data)
        elif choice == HIGHEST_SALES:
            value, name = highest_sales(makeup_data)
            print(f'Person with Highest Sale: {name}')
            print(f'Highest Sale: ${value:.2f}')
        elif choice == LOWEST_SALES:
            value, name = lowest_sales(makeup_data)
            print(f'Person with Lowest Sale: {name}')
            print(f'Lowest Sale: ${value:.2f}')
        elif choice == CALC_AVERAGE:
            value = calc_average(makeup_data)
            print(f'Average Sales: ${value:.2f}')
        elif choice == SAVE_STATS:
            save_stats(makeup_data)
        elif choice == QUIT:
            print("Exiting the program.")
            break

def read_csv(file: str) -> Dict[str, List]:
    """
    Reads a CSV file and parses the data into a dictionary.
    Each key is a column name, and the value is a list of column data.
    """
    try:
        with open(file, newline='', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            headers = next(reader)  # Get the column headers
            data = {header: [] for header in headers}  # Initialize dictionary

            for row in reader:
                data["Transaction"].append(int(row[0]))
                data["Name"].append(row[1])
                data["Date"].append(row[2])
                data["Product"].append(row[3])
                data["Bulk"].append(int(row[4]))
                data["Price"].append(float(row[5]))
                data["Location"].append(row[6])

            return data
    except Exception as e:
        print(f'Error reading CSV: {e}')
        return {}
    
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

def print_list(data: Dict[str, List]):
    
    print(f'{"Transaction":<15} {"Name":<15} {"Date":<15} {"Product":<15} {"Bulk":<10} {"Price":<10} {"Location":<15}')
    for i in range(len(data["Transaction"])):
        print(f'{data["Transaction"][i]:<15} {data["Name"][i]:<15} {data["Date"][i]:<15} {data["Product"][i]:<15} '
            f'{data["Bulk"][i]:<10d} {data["Price"][i]:<10.2f} {data["Location"][i]:<15}')

def highest_sales(data: Dict[str, List]) -> Tuple[float, str]:
    
    max_index = data["Price"].index(max(data["Price"]))  # Find the index of the max price
    return data["Price"][max_index], data["Name"][max_index]  # Return the price and name

def lowest_sales(data: Dict[str, List]) -> Tuple[float, str]:
    
    min_index = data["Price"].index(min(data["Price"]))  # Find the index of the min price
    return data["Price"][min_index], data["Name"][min_index]  # Return the price and name

def calc_average(data: Dict[str, List]) -> float:
    
    if data["Price"]:
        return sum(data["Price"]) / len(data["Price"])
    else:
        return 0

def save_stats(data: Dict[str, List]):

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