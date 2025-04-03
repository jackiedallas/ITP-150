"""
add_ice_cream.py
@author: Jackie Johnson-Dallas
This script creates the ice_cream.txt file and writes to it using
Python's IO library. Functions are used to get the user input and
exception handlers are used where needed.
"""

def main():
    
    # Create  a variable to control the loop
    run_program = 'y'
    found_file = False
    print("Let's update the ice cream inventory!")
    
    # Add records to the file
    while run_program.lower() == 'y':
        found_file = write_to_the_file()
        if not found_file:
            print("Sorry, we can't create the ice cream file at this time.")
            run_program = 'n'
        else:
            # Ask user if they want another flavor
            print("Do you want to add another flavor? ")
            run_program = input('Y for yes, anything else for No: ')
    if found_file:
        print_ice_cream_file('ice_cream.txt')
        
def write_to_the_file():
    try:
        with open('ice_cream.txt', mode='a') as ice_cream_file:
            # get ice cream info
            ice_cream = input_ice_cream()
            quarts = input_quarts()
            
            # append to ice_cream.txt
            ice_cream_file.write(ice_cream + '\n')
            ice_cream_file.write(str(quarts) + '\n')
            print("Ice cream information saved to file!")
        found_file = True
        return found_file
    except IOError:
        print("File not found or path incorrect.")
        found_file = False
        return found_file
    except Exception as err:
        print("An error occurred: ", err)
        
def input_ice_cream():
    ice_cream = input('Enter the flavor of ice cream: ')
    return ice_cream

def input_quarts():
    while True:
        try:
            quarts = int(input('Enter the quarts: '))
            if quarts <= 0:
                raise Exception
            else:
                return quarts
        except ValueError:
            print("Invalid, you must enter an integer greater than zero: ")
        except Exception:
            print("Invalid, enter a value greater than zero: ")
            
def print_ice_cream_file(filename):
    try:
        print(f"Here are the '{filename}' contents:")
        with open(filename, mode='r') as reader:
            for line in reader:
                print(line, end='')
    except IOError:
        print("File not found or path is incorrect..")
    except Exception as err:
        print('An error occurred: ', err)
        
if __name__ == '__main__':
    main()