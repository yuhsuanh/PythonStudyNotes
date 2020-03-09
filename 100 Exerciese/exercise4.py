#!/usr/bin/python3
# coding=utf-8

'''
	Python Exercise 4.

	Input date (year, month and day) to calculate the date is how days in this year.
'''

year = int(input('Year: '))
month = int(input('Month: '))
day = int(input('Day: '))
total = 0

monthsDay = [31,28,31,30,31,30,31,31,30,31,30,31]

if year%4 == 0 :
	total += 1;
print('total', total)

for i in range(0,month-1):
	total += monthsDay[i]
	print('total', total)

if month == 2 and day == 29:
	total -= 1

total += day
print('total', total)