#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
	This lab learn what is import
	And change variable
	1. In some1.py 'name' is sting which can't be cahnged
	2. In some2.py 'list' can be changed
'''

import some1
# print some1.py variable name
print(some1.name)
# get variable from some1.py to there
from some1 import name
print(name)
# change variable value
name = 'Yun-Ju Lai'
print(name)
# print some1.py variable name
print(some1.name)

print('')

import some2
# get variable from some2.py to there
from some2 import list
print(list)
# change variable value
list[0] = 100
# print this variable
print(list)
# print some2.py variable
print(some2.list)


# import 2 module
import some1, some2
# import all module
# import *

print('')

#imp.reload used to re execute module
import imp
imp.reload(some1)
imp.reload(some2)

# NOT import, NOT reload
# Just read codes and execute
exec(open('some1.py').read())


# try to import some3.py
# it will not do anything
import some3
