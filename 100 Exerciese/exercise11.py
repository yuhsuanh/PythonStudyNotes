#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 11.

	There have a couple rabbit. After 3 month they will born one pair rabbit.
	Example: 1,1,2,3,5,8,13,21...
'''

f1 = 1
f2 = 1
index = int(input('Input index: '))

for i in range(1,index+1):
	if i == 1 or i == 2:
		print(1)
	else:
		print(f1+f2)
		f2 = f1 + f2
		f1 = f2 - f1 


