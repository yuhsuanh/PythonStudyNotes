#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 18.

	Enter how many number of digits (i), and the digit number (n)
'''

num = int(input('Number(1-9): '))
digits = int(input('Digits: '))
sum = 0
temp = ''
arr = []

for i in range(digits):
	temp = temp + str(num)
	arr.append(temp)

print(arr)

for i in arr:
	sum += int(i)

print(sum)