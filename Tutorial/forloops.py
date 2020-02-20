#!/usr/bin/python3
# coding=utf-8

'''
	Python For Loops
		A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

'''

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
	print(x)

# Looping Through a String
print()
for x in fruits[0]:
	print(x)

# The break statement
print()
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
	print(x)
	if x == 'banana':
		break

# The continue statement
print()
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
	if x == 'banana':
		continue
	print(x)

# The range() function
print()
for x in range(6):
	print(x)
print()
for x in range(3, 6):
	print(x)
print()
for x in range(2, 15, 3):
	print(x)

# Else in For loop
print()
for x in range(6):
	print(x)
else:
	print('finish')

# Nested Loops
print()
for x in range(3):
	for y in range(5):
		print(x, y)

# Pass (nothing need to do in loop)
print()
for x in range(3):
	pass
