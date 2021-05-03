#Import Python Packages
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def processString(obj):
	if not obj:
		return ""
	else:
		return obj.text.strip();

def randomDelay():
	delay = random.random()*6
	# print(delay)
	time.sleep(delay)

def processAddressString(address):
	return address.replace(",", " ")

def getAreaClinics(basicUrl, listUri, filePath):
	print(filePath)

	wfile = open(filePath, "w")
	wfile.write('Store,phone,email,address,website\n')

	# ================ First Part Get Pharmacies List ================
	pharmaciesUri = []

	url = basicUrl + listUri
	response = requests.get(url)

	# Parser start here
	html = BeautifulSoup(response.text, "html.parser")
	tds = html.select(".serviceListing")

	for td in tds:
		a = td.select_one('a')
		pharmaciesUri.append(a['href'])

	randomDelay()
	# print(pharmacies)

	# ================ Second Part Get Each Pharmacy Information ================
	count=1
	for uri in pharmaciesUri:
		print('Store count: ' + str(count))
		count += 1;

		response = requests.get(basicUrl+uri)
		html = BeautifulSoup(response.text, "html.parser")

		name = processString(html.select_one('#ctl00_ContentPlaceHolder1_tdProgram'))
		phone = processString(html.select_one('#ctl00_ContentPlaceHolder1_lblOfficePhone'))
		email = processString(html.select_one('#ctl00_ContentPlaceHolder1_lnkEmail'))
		website = processString(html.select_one('#ctl00_ContentPlaceHolder1_lnkUrl'))
		address = processString(html.select_one('#ctl00_ContentPlaceHolder1_lblAddress'))

		line = name + "," + phone + "," + email + "," + processAddressString(address) + "," + website + "\n"
		wfile.write(line)
		randomDelay()

	wfile.close()



pharmaciesListUri = 'listservices.aspx?id=10072'

# --- 1. Erie St. Clair Area ---
print("1. Erie St. Clair Area")
eriestclairhealthline = 'https://www.eriestclairhealthline.ca/'
eriestclairFile = '1. Erie St. Clair Area.csv'
getAreaClinics(eriestclairhealthline, pharmaciesListUri, eriestclairFile)

# --- 2. South West Area ---
print('2. South West Area')
southwesthealthline = 'https://www.southwesthealthline.ca/'
southwestFile = '2. South West Area.csv'
getAreaClinics(southwesthealthline, pharmaciesListUri, southwestFile)

# --- 3. Waterloo Wellington Area ---
print('3. Waterloo Wellington Area')
wwhealthline = 'https://www.wwhealthline.ca/'
wwFile = '3. Waterloo Wellington Area.csv'
getAreaClinics(wwhealthline, pharmaciesListUri, wwFile)

# --- 4. Hamilton Niagara Haldimand Brant Area ---
print('4. Hamilton Niagara Haldimand Brant Area')
hnhbhealthline = 'https://www.hnhbhealthline.ca/'
hnhbFile = '4. Hamilton Niagara Haldimand Brant Area.csv'
getAreaClinics(hnhbhealthline, pharmaciesListUri, hnhbFile)

# --- 5. Central West Area ---
print('5. Central West Area')
centralwesthealthline = 'https://www.centralwesthealthline.ca/'
centralwestFile = '5. Central West Area.csv'
getAreaClinics(centralwesthealthline, pharmaciesListUri, centralwestFile)

# --- 6. Mississauga Halton Area ---
print('6. Mississauga Halton Area')
mississaugahaltonhealthline = 'https://www.mississaugahaltonhealthline.ca/'
mississaugahaltonFile = '6. Mississauga Halton Area.csv'
getAreaClinics(mississaugahaltonhealthline, pharmaciesListUri, mississaugahaltonFile)

# --- 7. Toronto Central Area --- 
print('7. Toronto Central Area')
torontocentralhealthline = 'https://www.torontocentralhealthline.ca/'
torontocentralFile = '7. Toronto Central Area.csv'
getAreaClinics(torontocentralhealthline, pharmaciesListUri, torontocentralFile)

# --- 8. Central Area ---
print('8. Central Area')
centralhealthline = 'https://www.centralhealthline.ca/'
centralFile = '8. Central Area.csv'
getAreaClinics(centralhealthline, pharmaciesListUri, centralFile)

# --- 9. Central East Area ---
print('9. Central East Area')
centraleasthealthline = 'https://www.centraleasthealthline.ca/'
centraleastFile = '9. Central East Area.csv'
getAreaClinics(centraleasthealthline, pharmaciesListUri, centraleastFile)

# --- 10. South East Area ---
print('10. South East Area')
southeasthealthline = 'https://www.southeasthealthline.ca/'
southeastFile = '10. South East Area.csv'
getAreaClinics(southeasthealthline, pharmaciesListUri, southeastFile)

# --- 11. Champlain Area ---
print('11. Champlain Area')
champlainhealthline = 'https://www.champlainhealthline.ca/'
champlainFile = '11. Champlain Area.csv'
getAreaClinics(champlainhealthline, pharmaciesListUri, champlainFile)

# --- 12. North Simcoe Muskoka Area ---
print('12. North Simcoe Muskoka Area')
nsmhealthline = 'https://www.nsmhealthline.ca/'
nsmFile = '12. North Simcoe Muskoka Area.csv'
getAreaClinics(nsmhealthline, pharmaciesListUri, nsmFile)

# --- 13. North East Area ---
print('13. North East Area')
northeasthealthline = 'https://www.northeasthealthline.ca/'
northeastFile = '13. North East Area.csv'
getAreaClinics(northeasthealthline, pharmaciesListUri, northeastFile)

# --- 14. North West Area ---
print('14. North West Area')
northwesthealthline = 'https://www.northwesthealthline.ca/'
northwestFile = '14. North West Area.csv'
getAreaClinics(northwesthealthline, pharmaciesListUri, northwestFile)
