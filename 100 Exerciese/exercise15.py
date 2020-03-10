#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 15.

	Change percent grade to letter grade
	grade greater than or equal to 90 is 'A'
	60-89 is 'B'
	less than 60 is 'C'
'''

score = int(input('Input Score:'))

if score >= 90:
	print('A')
elif score >= 60 and score < 90:
	print('B')
else:
	print('C')