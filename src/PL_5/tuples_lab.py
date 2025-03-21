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
tuple1 = tuple1 + (9,)
print('Contents of tuple1', tuple1)
print('Object ID for tuple1', id(tuple1))
print('Type of tuple1', type(tuple1))
print('tuple1 at index 4 -->', tuple1[4])

print('\n')

print('Task 5. Add new items at specific indexes to tuple1')
tuple1 = tuple1[:3] + (15, 20, 25) + tuple1[:5]
print('Contents of tuple1 after adding the 15, 20, 25, and first 5 elements to the end of tuple1\n', tuple1)
print('Object ID for tuple1', id(tuple1))

print('\n')

print('Task 6. Convert tuple1 to list1')
list1 = list(tuple1)
print('Contents of list1', list1)
print('Object ID of list1', id(list1))

print('\n')

print('Task 7. Append an item to the list')
list1.append(30)
print('Contents of list1', list1)
print('Object ID of list1', id(list1))

print('\n')