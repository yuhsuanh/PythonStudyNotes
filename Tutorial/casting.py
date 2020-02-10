#!/usr/bin/python3
# coding=utf-8

'''
	Specify a Variable Type
	There may be times when you want to specify a type on to a variable. This can be done with casting.
	int()
		constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal 
	float()
		constructs a float number from an integer literal, a float literal or a string literal
	str()
		constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''


# int()
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(type(x), x)
print(type(y), y)
print(type(z), z, end='\n\n')

# float()
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(type(x), x)
print(type(y), y)
print(type(z), z)
print(type(w), w, end='\n\n')

# str()
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(type(x), x)
print(type(y), y)
print(type(z), z)
