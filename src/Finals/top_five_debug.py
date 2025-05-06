"""
top_five.py
@author: PUT YOUR NAME HERE
Date Created: May 5, 2025
This script prints the top 5 data breaches occurring in this century 
including the number of accounts affected, the company affected, and the year
the data breach occurred. It also prints the most accounts affected, and
the company having the most accounts affected, and the year it occurred.
When you finish debugging the script, you should have the following results:

CSO (Chief Security Officer) lists the top data breaches
of all time at this URL: 
https://www.csoonline.com/article/534628/the-biggest-data-breaches-of-the-21st-century.html
This script lists the top 5 companies experiencing data breaches, the
total accounts affected, and the year the breach occurred. It also lists
the company that had the most accounts affected in a data breach and the
year it occurred.
Aadhaar had 1,100,000,000 accounts affected.
Alibaba had 1,100,000,000 accounts affected.
LinkedIn had 700,000 accounts affected.
Sina Weibo had 538,000 accounts affected in 2020.
Yahoo had 3,000,000,000 accounts affected in 2013.
Most Accounts Affected               3,000,000,000
Company Affected                             Yahoo

You must use the functions given within your solution and pass down
arguments. No global variables are allowed.
"""


def main():  # Added missing parenthesis
    read_me()
    companies = ['Aadhaar', 'Alibaba', 'LinkedIn', 'Sina Weibo', 'Yahoo']  # Added missing single quote
    accounts = [1_100_000_000, 1_100_000_000, 700_000, 538_000, 3_000_000_000]
    print_companies(companies, accounts)  # added missing argument
    max_row = find_highest_index(companies, accounts)  # removed one equal sign
    print(f'{"Most Accounts Affected":30s}{accounts[max_row]:>20,d}')
    print(f'{"Company Affected":30s}{companies[max_row]:>20s}')


def read_me():  # added missing colon
    long_string = '''CSO (Chief Security Officer) lists the top data breaches
of all time at this URL: 
https://www.csoonline.com/article/534628/the-biggest-data-breaches-of-the-21st-century.html
This script lists the top 5 companies experiencing data breaches, the
total accounts affected, and the year the breach occurred. It also lists
the company that had the most accounts affected in a data breach and the
year it occurred.'''
    print(long_string)


def print_companies(companies, accounts):
    for row in range(len(companies)):
        print(companies, 'had', format(accounts[row], ',d'), 
            'accounts affected.')


def find_highest_index(companies, accounts):  # added 'def' to the function name
    max_accounts = accounts[0]
    max_index = 0

    for row in range(len(companies)):
        if accounts[row] == max_accounts:
            max_accounts = accounts[row]
            max_index = max_index
    return max_index


if __name__ == '__main__':
    main()
