#!/usr/bin/python3
# coding=utf-8

'''
	Python Lists
	There are four collection data types in the Python programming language
	1. List is a collection which is ordered and changeable. Allows duplicate members.
	2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
	3. Set is a collection which is unordered and unindexed. No duplicate members.
	4. Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
'''

# List
thislist = ['apple', 'banana', 'cherry']
print(thislist)

# Access items
thislist = ['apple', 'banana', 'cherry']
print(thislist[0])

# Negative indexing
thislist = ['apple', 'banana', 'cherry']
print(thislist[-1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:6])
print(thislist[:5])
print(thislist[5:])

# Range of negative indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-6:-2])
print(thislist[:-5])
print(thislist[-5:], end='\n\n')


# Change item value
thislist = ['apple', 'banana', 'cherry']
thislist[0] = 'strawberry'
print(thislist)

# Loop thrugh a list
thislist = ['apple', 'banana', 'cherry']
for fruit in thislist:
	print(fruit)

# Check the item exists in the list
thislist = ['apple', 'banana', 'cherry']
if 'apple' in thislist:
	print('apple is in the list')

# List length
thislist = ['apple', 'banana', 'cherry']
print(len(thislist), end='\n\n')

# Add Items
thislist = ['apple', 'banana', 'cherry']
thislist.append('kiwi')
print(thislist)

# Add item with index
thislist = ['apple', 'banana', 'cherry']
thislist.insert(1, 'kiwi')
print(thislist)

# Remove item
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

# Pop to removes last item
thislist = ['apple', 'banana', 'cherry']
thislist.pop()
print(thislist)

# use del to delete item by index
thislist = ['apple', 'banana', 'cherry']
del thislist[0]
print(thislist)

# del also can delete whole list, can't not be used if delete
# thislist = ['apple', 'banana', 'cherry']
# del thislist
# print(thislist)

# use clear to remove all items
thislist = ['apple', 'banana', 'cherry']
thislist.clear()
print(thislist, end='\n\n')


# Copy List
thislist = ['apple', 'banana', 'cherry']
mylist = thislist.copy()
print(mylist)

thislist = ['apple', 'banana', 'cherry']
mylist = list(thislist)
print(mylist, end='\n\n')


# Join two lists
# method 1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# method 2 use for loop
for x in list2:
	list1.append(x)
print(list1)
#method 3 extend to connect two lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list1.extend(list2)
print(list1, end='\n\n')

# The list() Constructor
thislist = list(('apple', 'banana', 'cherry'))
print(thislist)