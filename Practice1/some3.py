#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
	This .py file only execute main() by some3.py (not be executed by import)
'''

def doSome(text):
	return text + '...processed...'

def main():
	fixture = 'orz'
	print(doSome(fixture))	

if __name__ == '__main__':
	main()