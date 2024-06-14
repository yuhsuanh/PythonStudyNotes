#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 14.

	Input a number and try to do prime factorization and print all prime factors
'''
import math

factors = []

def isPrimeNumer(num):
	#print(num, int(math.sqrt(num))+1)
	for i in range(2, int(math.sqrt(num))+1):
		if num % i == 0:
			return bool(0)
	return bool(1)

def primeFactorization(num):
	print('num', num)
	if isPrimeNumer(num) == bool(1):
		print('append out', num)
		factors.append(num)
		return
	for i in range(2, int(math.sqrt(num))+1):
		print('i', i)
		if num % i == 0:
			if isPrimeNumer(i) == bool(1):
				print('append in', i)
				factors.append(int(i))
			primeFactorization(num/i)
			num = num/i
	


num = int(input('Input a number:'))
primeFactorization(num)

print(factors)
