"""
hello_world.py
@author: Jackie Johnson-Dallas
Created January 21, 2025
This script will display hello world on the console.
"""


def hello_world(name='New Student'):
    """
    Prints Hello World with a default name
    or with a name passed to the function.
    """
    print(f"{name.title()}, Hello World from ITP-150!")


hello_world("jackie")
hello_world()
