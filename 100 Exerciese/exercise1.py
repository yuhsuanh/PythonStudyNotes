#!/usr/bin/python3
# coding=utf-8

'''
	Python Exercise 1.

	There are four digits: 1, 2, 3, 4.
	How many different three-digit numbers these digits can make up
'''

for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i != j) and (i != k) and (j != k):
				print(i, j, k)