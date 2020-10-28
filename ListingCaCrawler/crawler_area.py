#!/usr/bin/python3
# coding=utf-8

'''
	Install Packages:
		pip3 install requests
		pip3 install beautifulsoup4

'''

#Import Packages
import re
import requests 
from bs4 import BeautifulSoup


r= requests.get("https://listing.ca/")

soup = BeautifulSoup(r.text, "html.parser")
items = soup.select('.menu_item a')

print(len(items))


for item in items:
	print(item['href'])