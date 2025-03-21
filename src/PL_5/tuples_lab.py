"""
tuples_lab.py
@author: Jackie Johnson-Dallas
"""

print('\n')

print('Task 1. Create a tuple1 with different data types.')
tuple1 = ('tuple', False, 2.4, 1)
print('Contents of tuple1:', tuple1)
print('Object ID for tuple1', id(tuple1))

print('\n')

print('Task 2. Access tuple1 element by its index')
print('tuple1 at index 0 is', tuple1[0])

print('\n')

print('Task 3. Unpack tuple1 into several different variables.')
item1, item2, item3, item4 = tuple1
print(item1, item2, item3, item4)

print('\n')

print('Task 4. Add a new element with a value of 9 to tuple1 and see that a new object ID is created.')
