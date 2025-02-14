"""
sentinel_value_loop.py
@author: Jackie Johnson-Dallas
"""

grand_total = 0
run_program = input("Please enter 'Yes' to run the program or 'q' to quit. ")


while run_program.lower() == 'yes':
    if run_program == 'q':
        break
    MAX_NUM = 5
    total = 0
    print(f"This program calculates the sum of {MAX_NUM} numbers.")

    for counter in range(0, MAX_NUM, 1):
        print('-------- Number ', (counter + 1), '---------')
        num = input('Enter a whole number: ')
        if num == 'q':
            run_program = 'q'
            break
        else:
            total += int(num)
        print(total)
