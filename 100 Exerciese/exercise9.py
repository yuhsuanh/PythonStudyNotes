#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 9.

	Between print each number delay 1 second
'''

import time

chars = {1:'a', 2:'b', 3:'c'}

for key, value in chars.items():
	print(key, value)
	time.sleep(1)

for char in chars:
	print(char, chars[char])
	time.sleep(1)