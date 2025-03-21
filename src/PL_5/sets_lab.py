"""
sets_lab.py
@author: Jackie Johnson-Dallas
A set is a collection which is unordered, unchangeable, and unindexed. 
Set items are immutable, but you can remove items and add new items.
"""

from faker import Faker  # type: ignore

fake = Faker()


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

print('Task 2. Union | which gives items from both sets but does not allow  a duplicate')
seta = setx | sety  # note the union operator
print(seta)
print(id(seta))

print('\n')

print('Task 3. Add an element to the set.')
seta.add('red')
print(seta)
print(id(seta))

print('\n')

print('Task 4. Difference - which gives values not common in both sets.')
setb = seta - sety # note the - difference operator
print(setb)

print('\n')

print('Task 5. Take a list with duplicate items and make a set from it in order to remove the duplicate items and then assign again as a list with the same name as the originial list.')
list1 = [fake.first_name().lower() for _ in range(25)]
print('Length of List 2:', len(list1))
for index, name in enumerate(list1):
    print(f"{index}: {name}")
# print('list1 contents', list1)
# print('list1 ID', id(list1))
print('\n')
set1 = set(list1)
# print('set1 contents', set1)
# print('set1 ID', id(set1))

list2 = [fake.first_name().lower() for _ in range(25)]
print('Length of List 2:', len(list2))
for index, name in enumerate(list2):
    print(f"{index}: {name}")
# print('list2 contents', list2)
# print('list2 ID', id(list2))
print('\n')
set2 = set(list2)
# print('set1 contents', set2)
# print('set1 ID', id(set2))

set3 = set1 | set2
list3 = list(set3)
print('Length of unique combined list:', len(list3))
for index, name in enumerate(list3):
    print(f"{index}: {name}")
# print('result of adding list1 and list2 together without duplicates', list3)
# print('length of list 3', len(list3))

