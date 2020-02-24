#!/usr/bin/python3
# coding=utf-8

'''
	Python Lambda
		A lambda function is a small anonymous function.
		A lambda function can take any number of arguments, but can only have one expression.
	
	Syntax
		lambda arguments : expression
'''

# One argument
x = lambda a : a + 10
print(x(5))

# Two arguments
x = lambda a, b : a * b
print(x(3, 5))


'''
	Why Use Lambda Functions?
	The power of lambda is better shown when you use them as an anonymous function inside another function.
'''
def myfunc(n):
	return lambda a : a * n

doubler = myfunc(2)
tripler = myfunc(3)

print(doubler(11))
print(tripler(11))