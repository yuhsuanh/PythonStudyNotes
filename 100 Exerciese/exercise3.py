#!/usr/bin/python3
# coding=utf-8

'''
	Python Exercise 3.

	A number which add 100 is a perfect square
	, then the number add 168 also is a perfect square
'''
import math

# assume the number between 1-100
for num in range(1,100):

	temp = num + 100
	#print(math.sqrt(temp) % 1);
	if(math.sqrt(temp)%1 == 0):
		temp += 168
		if(math.sqrt(temp)%1 == 0):
			print(num)