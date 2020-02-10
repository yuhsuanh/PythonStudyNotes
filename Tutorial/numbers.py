#!/usr/bin/python3
# coding=utf-8

'''
	Python Numbers
	There are three numeric types in Python:
		int
		float
		complex
'''

x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x), x)
print(type(y), y)
print(type(z), z, end='\n\n')

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 64767611256479781123
z = -3255522
print(type(x), x)
print(type(y), y)
print(type(z), z, end='\n\n')


# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10000
y = 1.0
z = -35.596483214
print(type(x), x)
print(type(y), y)
print(type(z), z)
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E-4
z = -87.7e100
print(type(x), x)
print(type(y), y)
print(type(z), z, end='\n\n')


# Complex
# Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j
print(type(x), x)
print(type(y), y)
print(type(z), z, end='\n\n')


# Type Conversion
x = 10
y = 2.8
a = float(10)
b = int(y)
print(type(x), x)
print(type(a), a)
print(type(y), y)
print(type(b), b, end='\n\n')


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers
import random
print(random.randrange(1, 10)) # Between 1 and 9

