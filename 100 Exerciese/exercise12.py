#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 12.

	How many numbers are the prime numbers between 101 and 200.
'''
import math

def isPrimeNumer(num):
	for i in range(2, int(math.sqrt(num))+1):
		if num % i == 0:
			return bool(0)
	return bool(1)

count = 0
for i in range(101, 200):
	if isPrimeNumer(i) == bool(1):
		count += 1
		print(i)

print('Total:', count)