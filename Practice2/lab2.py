#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
	It will learn how to output information
'''

print(1, 2, 3)
# sep can assign which character between these variables
print(1, 2, 3, sep=',')
# end can assign what you want to put in the end
print(1, 2, 3, sep='<', end='\n\n')
# file can be used to output information to file
print(1, 2, 3, file = open('test.log', 'w'))
# use a will append to the end of the file
print('Yu-Hsuan Huang', file = open('test.log', 'a')) 


text = '%d %.2f %s' % (1, 99.35, 'Hsuan')
# output format
print(text)
print('%d %.4f %s' % (1, 99.35, 'Hsuan'))


# if want to read file

# Read whole file
name = input('Please input file name (test.log): ')
file = open(name, 'r', encoding='utf-8')
content = file.read()
print(content)
file.close()

# Read file by line - Method 1
name = input('Please input file name (test.log): ')
file = open(name, 'r', encoding='utf-8')
while True:
	line = file.readline()
	# capture StopIteration will break loop
	if not line: 
		break
	print(line, end='')
file.close()

# Read file by line - Method 1
# It will auto close the file
name = input('Please input file name (test.log): ')
for line in open(name, 'r', encoding='utf-8'):
	print(line, end='')
