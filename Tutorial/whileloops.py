#!/usr/bin/python3
# coding=utf-8

'''
	Python Loops
		while loops
		for loops

	The while Loop
		With the while loop we can execute a set of statements as long as a condition is true.
'''

i = 1
while i < 6:
	print(i)
	i += 1

# The break statement
print()
i = 1
while i < 6:
	print(i)
	if i == 3:
		break
	i += 1

# The continue statement
print()
i = 0
while i < 6:
	i += 1
	if i == 3:
		continue
	print(i)

# The else statement
print()
i = 1
while i < 6:
	print(i)
	i += 1
else:
	print('i is no longer less than 6')