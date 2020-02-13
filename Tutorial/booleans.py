#!/usr/bin/python3
# coding=utf-8

'''
	Python Boolean
	Booleans represent one of two values: True or False.
'''


print(10 > 9)
print(10 == 9)
print(10 < 9, end='\n\n')

# When you run a condition in an if statement, Python returns True or False
a = 100
b = 20
if a > b:
	print('a is greater than b', end='\n\n')
else:
	print('a is not greater than b', end='\n\n')


# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool('Hello'))
print(bool(15))
# Any string is True, except empty strings.
# Any number is True, except 0.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(''))
print(bool(()))
print(bool([]))
print(bool({}))

# Function can return boolean
def myFunc() :
	return True
print(myFunc(), end='\n\n')

# isinstance()
x = 200
print(isinstance(x, int))
print(isinstance(x, str))