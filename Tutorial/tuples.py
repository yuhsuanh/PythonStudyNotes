#!/usr/bin/python3
# coding=utf-8

'''
	Python Tuple
	A tuple is a collection which is ordered and 'unchangeable'. In Python tuples are written with round brackets.
'''

# Create a tuple
thistuple = ('apple', 'banana', 'cherry')
print(thistuple);

# Access tuple items
thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])
print(thistuple[-3:-1])

# Change Tuple values
x = ('apple', 'banana', 'cherry')
y = list(x)
y[0] = 'kiwi'
x = tuple(y)
print(x, end='\n\n')

# Loop through a tuple
thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
	print(x)

# Check if item exists
thistuple = ('apple', 'banana', 'cherry')
if 'banana' in thistuple:
	print('banana is exists in this tuple')

# Length of Tuple
thistuple = ('apple', 'banana', 'cherry')
print(len(thistuple), end='\n\n')


# Create Tuple with one item
thistuple = ('apple',) # must have a common in the last
print(type(thistuple))
thistuple = ('apple',) # ???
print(type(thistuple))

# Join two tuples
tuple1 = ('apple', 'banana', 'cherry')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# The tuple() Constructor
thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple)