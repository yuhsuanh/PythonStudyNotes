#!/usr/bin/python3
# coding=utf-8

'''
	Python Conditions and If statements

	Python supports the usual logical conditions from mathematics:
		Equals: a == b
		Not Equals: a != b
		Less than: a < b
		Less than or equal to: a <= b
		Greater than: a > b
		Greater than or equal to: a >= b

'''

# if statement
a = 1
b = 2
if b > a:
	print('b is greater than a')

# if no tab, it will raise an error.
#if b > a:
#print("b is greater than a")

# Elif
a = 1
b = 1
if b > a:
	print('b is greater than a')
elif a == b:
	print('a and b are equal')

# Else
a = 2
b = 1
if b > a:
	print('b is greater than a')
elif a == b:
	print('a and b are equal')
else:
	print('a is greater than b')


# Short Hand If
if a > b: print('a is greater than b')

# Short Hand If ... Else
a = 1
b = 2
print('A') if a > b else print('B', end='\n\n')


# And
a = 2
b = 1
c = 3
if a > b and c > a:
	print('Both condition are true')
if a > b or a > c:
	print('At least one of the conditions is true')


# Nested if
x = 18
if x > 10:
	print('Above 10')
	if x > 20:
		print('Above 20')
	else:
		print('Not Above 20')

# The Pass Statement
# if statement with no content, use "pass"
if a > b:
	pass

