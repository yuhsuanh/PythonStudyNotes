#Import Python Packages
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

websiteAddress = 'http://www.canadatransportation.com/'

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


def getCitiesList():
	resultDic = dict()

	uri = 'Freight_Brokers_Ontario_dwU.htm'
	response = requests.get(websiteAddress + uri)
	html = BeautifulSoup(response.text, "html.parser")
	citiesList = html.select_one(".citylisting").find_all('a')
	#print(citiesList)

	for city in citiesList:
		#print(city['href'] + "\t" + city.text)
		resultDic[city.text] = city['href']
	return resultDic


def companiesInCity(uri):
	resultList = list()

	response = requests.get(websiteAddress + uri)
	html = BeautifulSoup(response.text, "html.parser")
	companiesBlock = html.select('.companies')

	for companyBlock in companiesBlock:
		companyLink = companyBlock.select_one('.profilelink2').find('a')
		resultList.append(companyLink['href'])
		#print(companyLink)
	return resultList


def removeComma(text):
	resultText = text.replace(",", "").replace("\n", "").strip()
	return resultText


def getCompanyInfo(uri):
	response = requests.get(websiteAddress + uri)
	html = BeautifulSoup(response.text, "html.parser")

	html.select_one(".type2-heading")

	name = removeComma(html.select_one(".type2-heading").text)
	address = removeComma(html.select_one(".profile-address").text)
	phone = removeComma(html.select_one(".profile-tel").text)
	email = removeComma(html.select_one(".profile-email").text)
	return Company(name, phone, email, address)



#----- Main processing start from here -----
filePath = "ontario transportation company.csv"
wfile = open(filePath, "a")

transportationDic = getCitiesList();
for city, uri in transportationDic.items():
	print(city)
	companiesUriList = companiesInCity(uri)
	randomDelay()
	for companyUri in companiesUriList:
		company = getCompanyInfo(companyUri)
		print("\t" + company.name)
		wfile.write(company.__str__())
		randomDelay()
		
wfile.close()