#Import Python Packages
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

website = 'https://ontruck.org/'
uri = 'find-a-carrier'
page = '?p='

class Company:
	def __init__(self, name, phone, email, address):
		self.name = name
		self.phone = phone
		self.email = email
		self.address = address
	def __str__(self):
		return self.name + ',' + self.phone + ',' + self.email + ',' + self.address + '\n'


def randomDelay():
	delay = random.random()*5
	# print(delay)
	time.sleep(delay)

def removeComma(text):
	resultText = text.replace(",", "").replace("\n", "").strip()
	return resultText

def phoneNumFormat(text):
	resultText = text.replace("(", "").replace(") ", "-").strip()
	return resultText



#----- Main processing start from here -----
filePath = "ontario transportation company.csv"
wfile = open(filePath, "a")
# wfile.write('Store,phone,email,address\n')

# from 1 to 25
for pageNum in range(1, 26):
	print("Page: " + str(pageNum))
	response = requests.get(website + uri + page + str(pageNum))
	html = BeautifulSoup(response.text, "html.parser")
	companies = html.select('.sabai-entity-bundle-name-carrier-listing .sabai-row')

	for company in companies:
		emailBlock = company.select_one('.sabai-directory-contact-email')
		if emailBlock:
			name = removeComma(company.select_one('.sabai-directory-title').find('a').text)
			address = removeComma(company.select_one('.sabai-directory-location').text)
			phone = phoneNumFormat(removeComma(company.select_one('.sabai-directory-contact-tel').find('a').text))
			email = removeComma(emailBlock.find('a').text)
			company = Company(name, phone, email, address)
			print("\t" + name)
			wfile.write(company.__str__())
	randomDelay()

wfile.close()