"""
scope.py
@author.py: Jackie Johnson-Dallas
This program illustrates variable scope when using functions and the use of the
seldom used global keyword.
"""

x = 7 # sets x at the global scope

def main():
    # x = 7
    access_global()
    try_to_modify_global()
    print('x printed after try_to_modify_global is', x)
    modify_global()
    print('x printed after modify_global', x)
    try_to_modify_global()

def access_global():
    print('x printed from access_global', x)

def try_to_modify_global():
    x = 3.5 # local scope which overrides a global scope for x
    print('x printed from try_to_modify_global', x)

def modify_global():
    global x
    x = 'hello'
    print('x printed from modify_global:', x)
    
if __name__ == '__main__':
    main()