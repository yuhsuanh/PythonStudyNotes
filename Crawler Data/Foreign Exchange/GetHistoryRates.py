#Import Python Packages
import os
import time
import random
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# ===== Part 1
# requests.post(url, data={key: value}, json={key: value}, args)
# response = requests.get(link)

# startDate = '2015/01/01'
# endDate = '2015/12/01'
# link = "https://www.taifex.com.tw/cht/3/dailyFXRate"
# response = requests.post("https://www.taifex.com.tw/cht/3/dailyFXRate", data={'queryStartDate': startDate, 'queryEndDate': endDate})

# html = BeautifulSoup(response.text, "html.parser")
# print(html)

# ===== Part 2
# def minusOneDays(date):
# 	day = 1
# 	return date - timedelta(day)

# def minusDays(date):
# 	days = 300
# 	return date - timedelta(days)

# def dateformat(date):
# 	return date.strftime("%Y/%m/%d")

# def dateYear(date):
# 	year = date.strftime("%Y")
# 	return int(year)


# LINK = "https://www.taifex.com.tw/cht/3/dailyFXRate"

# startDate = datetime.now()
# endDate = minusDays(startDate)

# while dateYear(endDate) > 2014:
# 	print("Start Date: " + dateformat(startDate) + "\t End Date: " + dateformat(endDate))
# 	startDate = minusOneDays(endDate)
# 	endDate = minusDays(startDate)

	# response = requests.post(LINK, data={'queryStartDate': startDate, 'queryEndDate': endDate})
	# html = BeautifulSoup(response.text, "html.parser")

	# #Set delay time between request each page data
	# delay = random.random()*10
	# print(delay)
	# time.sleep(delay)


# ===== Part 
CURRENCIES = ["AUD","CAD","CHF","CNY","EUR","GBP","HKD","IDR","JPY","KRW","MYR","NZD","PHP","SEK","SGD","THB","USD","VND","ZAR"]
# CURRENCIES = ["AUD","CAD"]
TITLE = 'Date,Cash Buying Rate,Cash Selling Rate,Spot Buying Rate,Spot Selling Rate\n'
START_YEAR = 2019
END_YEAR = int(datetime.now().strftime("%Y"))
DATA_FILE_PATH_ROOT = "./data/"
DATA_FORMAT = ".csv"


# Change int month to two digits string format
def montheFormat(month):
	return "{:02d}".format(month)

# Create Last Year-Month string format base on today's year and today's month
def endYearMonthFormat():
	endYear = int(datetime.now().strftime("%Y"))
	endMonth = int(datetime.now().strftime("%m"))+1
	if endMonth == 13:
		endYear += 1
		endMonth = 1
	endDate = str(endYear)+"-"+montheFormat(endMonth)
	return endDate

# The file is exists or not
def isFileExist(filePath):
	file = os.path.isfile(filePath)
	if file:
		return True
	else:
		return False

def fileDateSet(filePath):
	dates = set()
	if isFileExist(filePath):
		#Read information from file
		file = open(filePath, 'rt')
		file.readline() #Read first line which is titles
		#Read all lines
		rows = file.readlines()
		#Run each line
		for row in rows:
			cols = row.split(',')
			if cols[0] not in dates:
				dates.add(cols[0])
		#Close read file
		file.close()
	return dates


# Get each currency data from web
def crawlerData(currency):
	print("======" + currency + "======")

	# Get end date (year-month)
	endDate = endYearMonthFormat()
	# Get file path
	filePath = DATA_FILE_PATH_ROOT + currency + DATA_FORMAT

	# Get data set
	dates = fileDateSet(filePath);

	if not isFileExist(filePath):
		wfile = open(filePath, 'w')
		wfile.write(TITLE)
	else:
		wfile = open(filePath, 'a')

	# Loop each year month
	for year in range(START_YEAR, END_YEAR+1):
		for month in range(1, 13):
			date = str(year)+"-"+montheFormat(month);
			if date == endDate:
				break

			# Request data start here
			link = "https://rate.bot.com.tw/xrt/quote/" + date + "/" + currency
			response = requests.get(link)
			html = BeautifulSoup(response.text, "html.parser")

			tbody = html.select_one(".table-bordered").select_one("tbody")
			trs = tbody.find_all('tr')

			for tr in trs:
				line = ""
				tds = tr.find_all('td')
				for td in tds:
					if td == tds[0]:
						dataDate = td.text
					#Skip dollar names
					if td == tds[1]:
						continue
					line += td.text.strip() + ","
				line = line[:-1] + "\n"
				# print(line)
				if dataDate not in dates:
					wfile.write(line)


			#Set delay time between request each page data
			delay = random.random()*8
			print(date + "\t" + "{:6.4f}".format(delay))
			time.sleep(delay)
	wfile.close()



for currency in CURRENCIES:
	crawlerData(currency);