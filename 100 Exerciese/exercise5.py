#!/usr/bin/python3
# coding=utf-8

'''
	Python Exercise 5.

	Input 3 integersm then print these numbers from min to max
'''

arr = []

for i in range(3):
	arr.append(int(input('numer: ')))

arr.sort()
print(arr)