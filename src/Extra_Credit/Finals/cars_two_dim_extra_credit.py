"""
cars_two_dim.py
Author: Jackie Johnson-Dallas
Date: 2023-10-01
Description: Reads a CSV file containing car data, processes it, and calculates descriptive statistics.
"""

import csv
from collections import Counter

DATA_FILE = 'Automobile_data_ITP150-1.csv'
OUTPUT_FILE = 'car_stats_refactor.csv'


def main():
    cars = read_csv(DATA_FILE)
    display_table(cars)

    manufacturer_counts = count_manufacturers(cars)
    display_counts(manufacturer_counts, "Standard Counting")

    collections_counts = Counter([row[0] for row in cars])
    display_counts(collections_counts, "Using Collections")

    write_counts_to_file(manufacturer_counts)


def read_csv(file_path):
    """
    Reads a CSV file and parses the data into a list of lists.
    Converts MPG to int and Price to float.
    """
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]

    for row in data:
        row[2] = int(row[2])     # MPG
        row[3] = float(row[3])   # Price

    return data


def display_table(data):
    print(f'{"Manufacturer":<20} {"Model":>20} {"MPG":>10} {"Price":>15}')
    for row in data:
        print(f'{row[0]:<20} {row[1]:>20} {row[2]:>10d} {row[3]:>15,.2f}')


def count_manufacturers(data):
    """
    Counts the number of cars per manufacturer using a basic dictionary.
    """
    counts = {}
    for row in data:
        manufacturer = row[0]
        counts[manufacturer] = counts.get(manufacturer, 0) + 1
    return counts


def display_counts(counts, title):
    print(f"\nCounts for each Manufacturer ({title})")
    print(f'{"Manufacturer":<20} {"Count":>10}')
    for manufacturer, count in sorted(counts.items()):
        print(f'{manufacturer:<20} {count:>10d}')
    print(f'Total Vehicles Counted: {sum(counts.values())}\n')


def write_counts_to_file(counts):
    with open(OUTPUT_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Manufacturer', 'Count'])
        for manufacturer, count in counts.items():
            writer.writerow([manufacturer, count])
    print(f'Manufacturer counts written to "{OUTPUT_FILE}".')


if __name__ == "__main__":
    main()
