"""
delete_ice_cream.py
@author: Jackie Johnson-Dallas
This script searches the ice_cream.txt file for a ice_cream entered therein
and deletes the record.
"""

import os

def main():
    # Create  a variable to control the loop
    run_program = 'y'
    found_file = False
    print("Let's delete from the ice cream inventory!")
    
    # search for records in the file
    while run_program.lower() == 'y':
        # get the search value
        ice_cream = input_ice_cream()
        found_file = delete_flavor(ice_cream, found_file)
        if not found_file:
            print('Sorry, we cannot search for ice cream at this time.')
            run_program = 'n'
        else:
            # ask the user if they want to search for another flavor
            print('Do you want to delete another flavor? ')
            run_program = input('Y for Yes, anything else for No: ')

def input_ice_cream():
    ice_cream = input('Enter the flavor of ice cream: ')
    return ice_cream

def delete_flavor(ice_cream, found_file):
    try:
        found_flavor = False
        # open the file
        ice_cream_file = open('ice_cream.txt', 'r')
        
        # open the temp file
        temp_file = open('temp.txt', 'w')
        
        # read the description for the first record
        flavor = ice_cream_file.readline()
        
        # read the rest of the file
        while flavor != '':
            # read the qty
            quarts = int(ice_cream_file.readline())
            
            # strip the new line from the description
            flavor = flavor.rstrip('\n')
            
            # if this is not the record to delete, then write it to the temp 
            # file
            if flavor != ice_cream:
                # write the record to the temp_file
                temp_file.write(flavor + '\n')
                temp_file.write(str(quarts) + '\n')
            else:
                # set the found flag to true
                found_flavor = True
            # read the next description
            flavor = ice_cream_file.readline()
        
        # close the ice cream file and the temp file
        ice_cream_file.close()
        temp_file.close()
        
        # delete the original ice cream file
        os.remove('ice_cream.txt')
        
        # rename the temp file
        os.rename('temp.txt', 'ice_cream.txt')
        
        # if the search value was found or not display messages
        if found_flavor:
            print('The ice cream file has been updated.')
        else:
            print('That flavor was not found in the file')
        
        found_file = True
        return found_file
    except IOError:
        print('The file could not be found or accessed.')
    except Exception as err:
        print('An error occurred.', err)
        
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

# call main function
main()