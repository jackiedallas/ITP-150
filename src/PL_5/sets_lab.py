"""
sets_lab.py
@author: Jackie Johnson-Dallas
A set is a collection which is unordered, unchangeable, and unindexed. 
Set items are immutable, but you can remove items and add new items.
"""

print('\n')

print('Task 1. Intersection & gives items common to both sets.')
setx = set(['green', 'blue'])
print(setx)

print('\n')

sety = set(['blue', 'yellow'])
print(sety)

print('\n')

setz = setx & sety  # Note the & intersection operator
print(setz)

print('\n')
