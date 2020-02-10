#!/usr/bin/python3
# coding=utf-8

'''
	Create Variables
'''
# Method 1
x = 5
y = 'Huang' # same as y = "Huang"
print(x)
print(y, end='\n\n')
# Method 2
x, y, z = 'Yu', 'Hsuan', 'Huang'
print(x)
print(y)
print(z, end='\n\n')
# Method 3
x = y = z = 'Yu-Hsuan Huang'
print(x)
print(y)
print(z, end='\n\n')



# Global Variables
# Method 1
# Create a variable outside of a function, and use it inside the function
x = 'Awesome'

def myfunc():
	print(x)

# Call Function myfunc
myfunc()
print(x)


# Method 2
# Identify x is global variable
def myfunc():
  global x
  x = "fantastic"
# Call Function myfunc
myfunc()
print(x, end='\n\n')
