#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 20.

	A ball falls from 100m, and bounce back to half of the original height after each landing	
'''

height = 100
total = 0

for i in range(10):
	if i == 0:
		total += height
	else:
		total += (height*2)
	print(height)
	height /= 2

print(total)