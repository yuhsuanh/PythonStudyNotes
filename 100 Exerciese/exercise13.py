#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 13.

	Narcissistic number : 3 digits
	Example: 153 is 1^3 + 5^3 + 3^3
'''

for i in range(100, 1000):
	a = pow(int(i/100), 3)
	b = pow(int((i%100)/10), 3)
	c = pow(i%10, 3)
	if a+b+c == i:
		print(i)