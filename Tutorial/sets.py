#!/usr/bin/python3
# coding=utf-8

'''
	Python Set
	A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
'''

thisset = {'apple', 'banana', 'cherry'}
print(thisset)

# Access items
thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
	print(x)
if 'banana' in thisset:
	print('banana is in this set', end='\n\n')


# Change Items
# Once a set is created, you cannot change its items, but you can add new items.
# Add Items
thisset = {'apple', 'banana', 'cherry'}
thisset.add('orange')
print(thisset)
thisset.update(['orange', 'mongo', 'grapes'])
print(thisset)
thisset.add('orange') # it will not add to the set if it is exist in the set
print(thisset)

# Remove Item
thisset = {'apple', 'banana', 'cherry'}
# If the item to remove does not exist, remove() will raise an error.
thisset.remove('banana')
print(thisset)
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard('cherry')
print(thisset)

# Pop the item
# Sets are unordered, so when using the pop() method, you will not know which item that gets removed.
thisset = {'apple', 'banana', 'cherry'}
thisset.pop()
print(thisset)

# Clear the Set
thisset.clear()
print(thisset)
# Deltet the Set (It will not exists anymore)
# thisset = {"apple", "banana", "cherry"}
# del thisset
# print(thisset)

# Join two sets
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 =  set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

# The set() Constructor
thisset = set(('apple', 'banana', 'cherry'))
print(thisset)
