#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 7.

	Copy one list all number to aonther list.
'''

a = [1,2,3,4,5,6,7]
b = []
c = []

print('a', a)

b = a[:]
print('b', b)
c = a.copy()
print('c', c)