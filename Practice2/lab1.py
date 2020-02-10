#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
	It will learn how to input information
'''

import sys
# Get input from command line argument
print('Hello ' + sys.argv[1] + '!')

# Python 2.7
'''name = raw_input('Please input your name: ')
print('Welcome ', name)'''

# Python3
name = input('Please input your name: ')
print('Welcome ', name)


