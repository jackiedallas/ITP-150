"""
cars_two_dim.py
@author: Jackie Johnson-Dallas
@date: 2023-10-01
@description: This script reads a csv file containing car data, processes it, and calculates descriptive statistics.
"""

import csv
import collections

DATA_FILE = 'Automobile_data_ITP150-1.csv'
OUTPUT_FILE = 'car_stats.csv'


def main():

    cars_two_dim = [[]]  # initialize a 2D list
    m_dict = {}  # initialize a dictionary
    cars_two_dim = read_csv(DATA_FILE)  # read the csv file
    print_list(cars_two_dim)  # print the list
    m_dict = get_dictionary(cars_two_dim)  # get the dictionary
    manufacturer_count_using_dict(m_dict, cars_two_dim)  # count the manufacturers
    manufacturer_count_using_collections(m_dict)  # count using collections
    write_dictionary_to_file(m_dict)  # write the dictionary to a file
    
    
def read_csv(file_name):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        file_name = [row for row in reader]
        
    # make mpg and price columns into integers and floats
    for row in range(len(file_name)):
        file_name[row][2] = int(file_name[row][2])
        file_name[row][3] = float(file_name[row][3])
        
    print(file_name)
    print("Number rows in the lsit:", len(file_name))
    return file_name

def print_list(file_name):
    print(f'{"Manufacturer":<20} {"Model":>20} {"MPG":>21} {"Price":>15}')
    for row in range(len(file_name)):
        print(f'{file_name[row][0]:<20s} {file_name[row][1]:>20}\
            {file_name[row][2]:>10d} {file_name[row][3]:>15,.2f}')

def get_dictionary(file_name):
    manufacturer_set = set()
    for row in range(len(file_name)):
        item = file_name[row][0]
        manufacturer_set.add(item)
    print('Manufacturer Set:', manufacturer_set)
    
    manufacturer_dict = dict.fromkeys(manufacturer_set, 0)
    print("Manufacturer Dictionary:", manufacturer_dict)
    return manufacturer_dict

def manufacturer_count_using_dict(dictionary, file_name):
    for each_key in dictionary:
        print(each_key)
        count = 0
        for each_row in range(len(file_name)):
            if file_name[each_row][0] == each_key:
                count += 1
                print('manufacturer is', each_key, 'count is', count)
                dictionary[each_key] = count
                
    print("Manufacturer Dictionary:", dictionary)
    x = sum(dictionary.values())
    print(x)
    print("Counts for each Manufacturer")
    print(f'{"Manufacturer":<20s} {"Count":>20s}')
    for x, y in dictionary.items():
        print(f'{x:<20s} {y:>20d}')

def manufacturer_count_using_collections(dictionary):
    print('Counts for each Manufacturer with Collections')
    m_dictionary = collections.Counter(dictionary)
    print(m_dictionary)
    sum_values = sum(m_dictionary.values())
    print('sum values:', sum_values)
    print("Counts for each Manufacturer")
    print(f'{"Manufacturer":<20s} {"Count":>20s}')
    for x, y in m_dictionary.items():
        print(f'{x:<20s} {y:>20d}')
        
def write_dictionary_to_file(dictionary):
    m_file = csv.writer(open(OUTPUT_FILE, 'w'))
    for key, value in dictionary.items():
        m_file.writerow([key, value])
    print('Dictionary written to file:', OUTPUT_FILE)
    
if __name__ == "__main__":
    main()
