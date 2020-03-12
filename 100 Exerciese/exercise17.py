#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 17.

	Enter a string and count how many the amount of english, space, number, others characters
'''

str = input('Enter a string: ')

letters = 0
spaces = 0
digits = 0
others = 0

for i in str :
	if i.isalpha():
		letters += 1
	elif i.isspace():
		spaces += 1
	elif i.isdigit():
		digits += 1
	else:
		others += 1

print('letters:', letters)
print('spaces:', spaces)
print('digits:', digits)
print('others', others)