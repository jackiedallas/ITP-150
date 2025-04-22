"""
population_increases.py
@author: Jackie Johnson-Dallas
Date: 2025-04-17
https://unicode.org/emoji/charts/full-emoji-list.html
"""

import csv
import os


def main():
    DISPLAY_LIST = 1
    STATS = 2
    SAVE_STATS = 3
    QUIT = 99
    pop_list = []
    pop_stats = {}
    choice = 0
    if not os.path.isfile('us_population.csv'):
        print('Error: us_population.csv file not found.')
    else:
        pop_list = read_csv('us_population.csv')
    if pop_list:
        while choice != QUIT:
            menu_string = 'Population Statistics Menu\n' \
                        '1. Display Population List\n' \
                        '2. Calculate and Display Statistics\n' \
                        '3. Save Statistics to File\n' \
                        '99. Quit'
            valid_choices = [DISPLAY_LIST, STATS, SAVE_STATS, QUIT]
            choice = input_menu_choice(menu_string, valid_choices)
            if choice == DISPLAY_LIST:
                display_list(pop_list)
            elif choice == STATS:
                pop_stats = calc_descriptive_stats(pop_list, pop_stats)
            elif choice == SAVE_STATS:
                save_stats(pop_stats)
        
def read_csv(file_name):
    """
    Reads a CSV file and returns a list of dictionaries.
    """
    try:
        with open(file_name, newline='') as pop_file:
            pop_reader = csv.reader(pop_file, delimiter=',')
            pop_list = [row for row in pop_reader]
        for row in range(1, len(pop_list)):
            pop_list[row][0] = int(pop_list[row][0])
            pop_list[row][1] = int(pop_list[row][1])
        return pop_list
    except IOError as ierr:
        print(f'An error occurred while reading the file: {ierr}')
    except IndexError as xerr:
        print(f'An index error occurred: {xerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        
def input_menu_choice(menu_string, valid_choices):
    while True:
        try:
            print('-'*50)
            print(menu_string)
            print('-'*50)
            choice = int(input('Enter your choice: '))
            if choice in valid_choices:
                return choice
            else:
                raise Exception
        except ValueError:
            print('Error: Please enter a valid number.')
        except Exception:
            print('Error: Please enter a valid choice from the menu.')
            print(f'Valid choices are: {valid_choices}')
            
def display_list(pop_list):
    print('='*35)
    print(f'{'As of Date':12s}{'pop':>20s}')
    try:
        for row in range(1, len(pop_list)):
            print(f'{pop_list[row][0]:12}{pop_list[row][1]:>20,d}')
        print('='*35)
    except IndexError as xerr:
        print(f'An index error occurred: {xerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')

def calc_descriptive_stats(pop_list, pop_stats):
    average_pop = calc_average(pop_list)
    lowest_pop, lowest_year = find_lowest(pop_list)
    highest_pop, highest_year = find_highest(pop_list)
    try:
        labels = ['Average Population', 'Lowest Population', 'Lowest Year',
                'Highest Population', 'Highest Year']
        stats = [average_pop, lowest_pop, lowest_year, highest_pop, highest_year]
        stats_zipped = zip(labels, stats)
        pop_stats = dict(stats_zipped)
        for key, val in pop_stats.items():
            print(f'{key:30s}{val:>20,.0f}')
        return pop_stats
    except KeyError as kerr:
        print(f'A key error occurred: {kerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        
def calc_average(pop_list):
    sum_pop = 0
    try:
        for row in range(1, len(pop_list)):
            sum_pop += pop_list[row][1]
        average_pop = sum_pop / (len(pop_list) - 1)
        return average_pop
    except ZeroDivisionError as zerr:
        print(f'A zero division error occurred: {zerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
    except IndexError as xerr:
        print(f'An index error occurred: {xerr}')
        
def find_lowest(pop_list):
    try:
        lowest_pop = pop_list[1][1]
        lowest_year = pop_list[1][0]
        for row in range(1, len(pop_list)):
            if pop_list[row][1] < lowest_pop:
                lowest_pop = pop_list[row][1]
                lowest_year = pop_list[row][0]
        return lowest_pop, lowest_year
    except IndexError as xerr:
        print(f'An index error occurred: {xerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        
def find_highest(pop_list):
    try:
        highest_pop = pop_list[1][1]
        highest_year = pop_list[1][0]
        for row in range(1, len(pop_list)):
            if pop_list[row][1] > highest_pop:
                highest_pop = pop_list[row][1]
                highest_year = pop_list[row][0]
        return highest_pop, highest_year
    except IndexError as xerr:
        print(f'An index error occurred: {xerr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
        
def save_stats(pop_stats):
    try:
        pop_stats_file = csv.writer(open('pop_stats.csv', 'w'))
        for key, val in pop_stats.items():
            pop_stats_file.writerow([key, val])
        print('Statistics saved to pop_stats.csv')
    except IOError as ierr:
        print(f'An error occurred while writing to the file: {ierr}')
    except Exception as err:
        print(f'An unexpected error occurred: {err}')
    except KeyError as kerr:
        print(f'A key error occurred: {kerr}')

if __name__ == '__main__':
    main()