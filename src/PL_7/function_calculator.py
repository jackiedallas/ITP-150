"""
function_calculator.py
@author: Jackie Johnson-Dallas
"""

def main():
    num_1 = 10
    num_2 = 3
    
    add_result = add_results(num_1, num_2)
    subtract_result = subtract_results(num_1, num_2)
    multiply_result = multiply_results(num_1, num_2)
    divide_result = divide_results(num_1, num_2)
    
    display_results(num_1, "+", num_2, "=", add_result)
    display_results(num_1, "-", num_2, "=", subtract_result)
    display_results(num_1, "x", num_2, "=", multiply_result)
    display_results(num_1, "/", num_2, "=", divide_result)
    
def add_results(num_1, num_2):
    return num_1 + num_2

def subtract_results(num_1, num_2):
    return num_1 - num_2

def multiply_results(num_1, num_2):
    return num_1 * num_2

def divide_results(num_1, num_2):
    return num_1 / num_2

def display_results(num_1, operator, num_2, equals, results):
    if type(results) == int:
        result = f"{num_1} {operator} {num_2} {equals} {results}"
        print(result)
    else:
        result = f"{num_1} {operator} {num_2} {equals} {results:.3f}"
        print(result)
        
# call main function
if __name__ == '__main__':
    main()
