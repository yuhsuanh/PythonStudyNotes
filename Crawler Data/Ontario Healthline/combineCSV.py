#Import Python Packages
import os
from os import listdir
from os.path import isfile, join

listPath = "./total/"
allFiles = [f for f in listdir(listPath) if isfile(join(listPath, f))]
print(allFiles)

wfile = open(listPath + 'total.csv', 'w')
wfile.write('Store,phone,email,address,website\n')

for file in allFiles:
	filePath = listPath + file
	print(filePath)

	rfile = open(filePath, 'rt')
	rfile.readline()

	rows = rfile.readlines()
	for row in rows:
		wfile.write(row)
	rfile.close()

wfile.close()


