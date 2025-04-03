"""
search_ice_cream.py
@author: Jackie Johnson-Dallas
This script searches the ice_cream.txt file. Functions are used to get the
user input and search the file.
Exception handlers are used where needed.
"""

def main():
    # Create variable to control loop
    run_program = 'y'
    print("Let's search the ice cream inventory!")
    
    # search for records in the file
    while run_program.lower() == 'y':
        # get the search value
        ice_cream = input_ice_cream()
        found_file = search_the_file(ice_cream)
        if not found_file:
            print('Sorry, we cannot search for ice cream at this time.')
            run_program = 'n'
        else:
            # ask the user if they want to search for another flavor
            print('Do you want to search for another flavor? ')
            run_program = input('Y for Yes, anything else for No: ')
    
def input_ice_cream():
    ice_cream = input('Enter the flavor of ice cream: ')
    return ice_cream

def search_the_file(ice_cream):
    try:
        found_flavor = False
        # open the file
        ice_cream_file = open('ice_cream.txt', 'r')
        flavor = ice_cream_file.readline()
        # read the rest of the file
        while flavor != '':
            # read the quarts field
            quarts = int(ice_cream_file.readline())
            # strip new line from end of ice cream file
            flavor = flavor.strip('\n')
            if flavor.lower() == ice_cream.lower():
                # display the record
                print('Ice Cream', flavor)
                print('Quarts', quarts, '\n')
                # set the found flag to True
                found_flavor = True
            flavor = ice_cream_file.readline()
        # close the file
        ice_cream_file.close()
        # display message if not found
        if not found_flavor:
            print('That flavor was not found in the file.')
        return True
    except IOError:
        print('The file could not be found or accessed.')
        return False
    except Exception as err:
        print('An error occured.', err)

if __name__ == '__main__':
    main()