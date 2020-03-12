#!/usr/bin/python3
# coding=utf-8
'''
	Python Exercise 16.

	Print different date format and calculate date
'''
import datetime

today = datetime.date.today()
print(today.strftime('%d/%m/%Y'))

defaultDate = datetime.date(1992, 9, 30)
print(defaultDate.strftime('%d/%m/%Y'))

#add one day
defaultDate = defaultDate + datetime.timedelta(days=1)
print(defaultDate.strftime('%d/%m/%Y'))

#change date
defaultDate = defaultDate.replace(year = defaultDate.year + 2)
print(defaultDate.strftime('%d/%m/%Y'))