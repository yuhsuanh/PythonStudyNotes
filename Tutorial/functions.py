#!/usr/bin/python3
# coding=utf-8

'''
	Python Functions
		A function is a block of code which only runs when it is called.
		You can pass data, known as parameters, into a function.
		A function can return data as a result.
'''

# Create a Function
def my_function1():
	print('Hello from a function')
# Calling a Function
my_function1()

# Arguments
def my_function2(fname):
	print('First Name: ' + fname)
my_function2('Yu-Hsuan')

def my_function3(fname, lname):
	print('Welcome ' + fname + ' ' + lname)
	print('Welcome ' + lname + ', ' + fname)
my_function3('Yu-Hsuan', 'Huang')


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
def my_function4(*kids):
	print('A kid name is ' + kids[1])
my_function4('Sean', 'Winnie', 'Amual')


# Keyword Arguments
def my_function5(child3, child2, child1):
	print("The youngest child is " + child3)
my_function5(child1 = 'Sean', child2 = 'Winnie', child3 = 'Amual')

# Arbitrary Keyword Arguments, **kwargs
def my_function6(**kid):
  print("His last name is " + kid["lname"])
my_function6(fname = "Yu-Hsuan", lname = "Huang")

# Default Parameter Value
def my_function7(country = 'Taiwan'):
	print('I am from ' + country)
my_function7()
my_function7('Canada')

# Return value
def my_function8(num):
	return num*2
print(my_function8(5), end = '\n\n')

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def function():
	pass


# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
def my_function9(x, y):
	if x % y == 0:
		result = x/y
		print(result)
		my_function9(result, y)
	else:
		result = x
	return result
my_function9(32, 4)