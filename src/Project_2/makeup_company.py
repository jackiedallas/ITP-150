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

def main():
    
    # Check if the data file exists
    if not os.path.isfile(DATA_FILE):
        print(f'Error: {DATA_FILE} file not found.')
        return
    
    makeup_list = read_csv(DATA_FILE) # initialize makeup list
    makeup_dictionary = {} # initialize makeup dictionary
    print(makeup_list)
    
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
    
    pass

def read_csv(file: str) -> List[List[int]]:
    try:
        with open(file, newline='') as f:
            reader = list(csv.reader(f))
            return [[int(trans), str(name), str(date), str(product), int(bulk), float(price), str(location)] for trans, name, date, product, bulk, price, location in reader[1:]]
    except Exception as e:
        print(f'Error reading CSV: {e}')
        return []
    
            

if __name__ == "__main__":
    main()