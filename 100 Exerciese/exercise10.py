#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 10.

	Print now date time, then delay 1 second print now date time
'''
import time
import datetime

now = datetime.datetime.now()
print(now)
print(now.strftime('%Y/%m/%d %H:%M:%S'))

time.sleep(1)

now = datetime.datetime.now()
print(now)
print(now.strftime('%Y/%m/%d %H:%M:%S'))