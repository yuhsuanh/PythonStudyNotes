#!/usr/bin/python3
# coding=utf-8

'''
	Install Packages:
		pip3 install requests
		pip3 install beautifulsoup4

'''

#Import Packages
import re
import time
import random

import requests 
from bs4 import BeautifulSoup



def getHistoryPriceData(area_list):
	# Table columns title
	table_titles = ['Year/Month', 'Number of Sales', 'Avg List Price', 'Avg Sold Price', 'Above/Below Asking', 'Price of Monthly Change', 'Percentage of Monthly Change', 'Days on Market']

	for area in area_list:
		print(area.capitalize())
		url = "https://" + area + ".listing.ca/real-estate-price-history.htm"
		# HTTP request to get HTML data, then use beautifulsoap to parser the HTML
		html = requests.get("https://barrie.listing.ca/real-estate-price-history.htm")
		soup = BeautifulSoup(html.text, "html.parser")

		#Get Title: "20XX Toronto Sales"
		titles = soup.find_all("div", string=re.compile(".* Sales"))
		titles_length = len(titles)

		#Get Table Data Values
		tables = soup.select(".tab_container table")
		tables_length = len(tables)

		#Parser Data
		if titles_length != tables_length:
			sys.exit(-1)
		else:
			#Print Each Columns Titles
			for title in table_titles:
				print(title, end="\t")
			print()

			#Determine if the length is the same
			if titles_length != tables_length:
				sys.exit(-1)
			else:
				#Using titles length and tables length to run for loop
				for index in range(0, titles_length):
					#Get each row
					trs = tables[index].find_all('tr')
					#Skip first tr because there're just titles
					for tr in trs[1:]:
						#Get each column in this row
						tds = tr.find_all('td')
						for td in tds:
							#If this is first td tag in this row, add the year before the month
							if tds.index(td) == 0:
								print(titles[index].text[0:4]+'/'+td.text, end="\t")
							else:
								print(td.text, end="\t")
						print()

		#Set delay time between request each page data
		delay = random.random()*4
		time.sleep(delay)



# area_list = ['barrie', 'brampton', 'burlington', 'caledon', 'clarington', 'hamilton', 'innisfil', 'kawartha-lakes', 'markham', 'milton', 'mississauga', 'oakville', 'oshawa', 'richmond-hill', 'toronto', 'vaughan']
area_list = ['barrie', 'markham', 'toronto']
getHistoryPriceData(area_list)

































# r= requests.get("https://barrie.listing.ca/real-estate-price-history.htm")

# #Print all HTML infomation
# # print(r.text)

# soup = BeautifulSoup(r.text, "html.parser")


# titles = soup.find_all("div", string=re.compile(".* Sales"))
# titles_length = len(titles)
# print('Title length', titles_length)
# # print(titles)
# # for title in titles:
# # 	print(title.string)

# # Table columns title
# table_titles = ['Year/Month', 'Number of Sales', 'Avg List Price', 'Avg Sold Price', 'Above/Below Asking', 'Price of Monthly Change', 'Percentage of Monthly Change', 'Days on Market']

# tables = soup.select(".tab_container table")
# tables_length = len(tables)
# print('Table length', len(tables))
# # print(talbes)
# # print(tables[1])

# for title in table_titles:
# 	print(title, end="\t")
# print()


# if titles_length != tables_length:
# 	sys.exit(-1)
# else:
# 	for index in range(0, titles_length):
# 		# titles[i].text
# 		trs = tables[index].find_all('tr')
# 		for tr in trs[1:]:
# 			tds = tr.find_all('td')
# 			for td in tds:
# 				if tds.index(td) == 0:
# 					print(titles[index].text[0:4]+'/'+td.text, end="\t")
# 				else:
# 					print(td.text, end="\t")
# 			print()
# #end



# trs = tables[0].find_all('tr')
# # print(len(trs))
# for tr in trs[1:]:
# 	tds = tr.find_all('td')
# 	# print(len(tds))
# 	for td in tds:
# 		if tds.index(td) == 0:
# 			print('year/'+td.text, end="\t")
# 		else:
# 			print(td.text, end="\t")
# 	print()
