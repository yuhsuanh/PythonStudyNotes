#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 8.

	Print 9x9 Multiplication table
'''

for i in range(1,10):
	for j in range(1,10):
		print(i,'*',j,'=',i*j, end='')
	print()