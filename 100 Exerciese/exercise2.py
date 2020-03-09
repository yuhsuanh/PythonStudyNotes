#!/usr/bin/python3
# coding=utf-8

'''
	Python Exercise 2.

	The Enterprise will give sales the commition base on the price which you sold this month.
	Less than or equal to 100,000 dollar -> 10% commition
	Greater than 100,000 dollar and Less than 200,000 -> within 100,000 part give 10% commition, above 100,000 part give 7.5%
	Greater than 200,000 dollar and Less than 400,000 -> between 200,000 and 400,000 give 5% commition
	Greater than 400,000 dollar and Less than 600,000 -> between 400,000 and 600,000 give 3% commition
	Greater than 600,000 dollar and Less than 1,000,000 -> between 600,000 and 1,000,000 give 1.5% commition
	Greater than 1,000,000 dollar -> over 1,000,000 part give 1% commition
	
	Using Keyboard to enter the sold price.
'''

price = int(input('Price: '))
priceRange = [1000000, 600000, 400000, 200000, 100000, 0]
commitionPercent = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
commition = 0

for idx in range(0,6):
	if price > priceRange[idx]:
		commition += (price-priceRange[idx]) * commitionPercent[idx]
		print((price-priceRange[idx]) * commitionPercent[idx])
		price = priceRange[idx]

print('---------')
print(commition)