#!/usr/bin/python3
# coding=utf-8

'''
	Python3 Array
		Python does not have built-in support for Arrays, but Python Lists can be used instead.
'''

cars = ['Ford', 'Toyota', 'BMW']
print(cars)
print(type(cars))
print(len(cars))

# Get item from array
print(cars[0])

# Modify the value
cars[0] = 'Ferrari'
print(cars[0], end='\n\n')

# Looping array elements
for x in cars:
	print(x)

# Adding Array Element
print()
cars.append('Kia')
for x in cars:
	print(x)

print()
print(cars.pop(1))
print(cars.remove('Kia'))
