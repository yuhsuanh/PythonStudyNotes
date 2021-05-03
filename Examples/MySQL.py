#Import Python Packages
import os
from bs4 import BeautifulSoup

import mysql.connector

def mysqlConnection():
	db_connection = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="1125",
		db = "tsx_stock"
	)
	return db_connection



# Get one result
def oneResult():
	db_connection = mysqlConnection()
	cursor = db_connection.cursor()
	cursor.execute("SELECT * FROM stock_type;")
	result = cursor.fetchone()
	print(result[0])
	db_connection.close()


# Get all results
def allResult():
	db_connection = mysqlConnection()
	cursor = db_connection.cursor()
	cursor.execute("SELECT * FROM stock_type;")
	results = cursor.fetchall()
	for d in results:
		id = d[0]
		name = d[1]
		print(str(id) + "\t" + name)

	for (id, name) in results:
		print(str(id) + '\t' + name)
	db_connection.close()


# Insert 
def insertRecord():
	db_connection = mysqlConnection()
	cursor = db_connection.cursor()
	name = "TEST_TYPE1"
	sql = "INSERT INTO stock_type (stock_type_name) VALUES (%s);" %(name)

# try:
	cursor.execute(sql)
	db_connection.commit()
# except:
	# print('*ERROR* ' + name + ' save stock_type to DB')

	db_connection.close()




















oneResult()
allResult()
insertRecord()
