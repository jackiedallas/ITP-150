import csv
import os
from typing import List, Dict, Tuple

# Constants
DISPLAY_LIST = 1
STATS = 2
SAVE_STATS = 3
QUIT = 99
DATA_FILE = 'us_population.csv'
OUTPUT_FILE = 'pop_stats.csv'


def main():
    
    
        
    if not os.path.isfile(DATA_FILE):
        print(f'Error: {DATA_FILE} file not found.')
        return

    pop_list = read_csv(DATA_FILE)
    if not pop_list:
        return

    pop_stats = {}
    choice = 0
    menu = (
        "Population Statistics Menu\n"
        "1. Display Population List\n"
        "2. Calculate and Display Statistics\n"
        "3. Save Statistics to File\n"
        "99. Quit"
    )

    while choice != QUIT:
        choice = input_menu_choice(menu, [DISPLAY_LIST, STATS, SAVE_STATS, QUIT])
        
        if choice == DISPLAY_LIST:
            display_list(pop_list)
        elif choice == STATS:
            pop_stats = calc_descriptive_stats(pop_list)
        elif choice == SAVE_STATS:
            save_stats(pop_stats)


def read_csv(file_name: str) -> List[List[int]]:
    try:
        with open(file_name, newline='') as f:
            reader = list(csv.reader(f))
            return [[int(year), int(pop)] for year, pop in reader[1:]]
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
            print(f'Invalid choice. Valid choices are: {valid_choices}')
        except ValueError:
            print('Error: Please enter a number.')

def display_list(pop_list: List[List[int]]) -> None:
    print('=' * 35)
    print(f'{"Year":<12}{"Population":>20}')
    for year, pop in pop_list:
        print(f'{year:<12}{pop:>20,}')
    print('=' * 35)

def calc_descriptive_stats(pop_list: List[List[int]]) -> Dict[str, float]:
    values = [pop for _, pop in pop_list]
    years = [year for year, _ in pop_list]
    average = sum(values) / len(values)
    min_val, min_year = min(pop_list, key=lambda x: x[1])
    max_val, max_year = max(pop_list, key=lambda x: x[1])

    stats = {
        'Average Population': average,
        'Lowest Population': min_val,
        'Lowest Year': min_year,
        'Highest Population': max_val,
        'Highest Year': max_year
    }

    for k, v in stats.items():
        print(f'{k:30s}{v:>20,.0f}')
    return stats

def save_stats(stats: Dict[str, float]) -> None:
    try:
        with open(OUTPUT_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            for key, val in stats.items():
                writer.writerow([key, val])
        print(f'Statistics saved to {OUTPUT_FILE}')
    except Exception as e:
        print(f'Error writing to file: {e}')

if __name__ == '__main__':
    main()
