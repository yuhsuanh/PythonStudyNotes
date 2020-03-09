#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 6.

	Fibonacci sequence
	example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
	i = i-2 + i-1
'''

def fib(num):
	if num == 0:
		return 0
	if num == 1:
		return 1
	return fib(num-1) + fib(num-2)

print(fib(int(input('Index (Fibonacci sequence): '))))