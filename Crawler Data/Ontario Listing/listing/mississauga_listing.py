#Import Python Packages
import os
import time
import random
import requests
from datetime import date
from bs4 import BeautifulSoup

'''
    Read file data and save id to set
    The ids set will use to determine if this data exist in the file
'''
#Id Set
ids = set()
filePath = "./data/mississauga-listing.csv"
today = str(date.today())


#File exists?
file = os.path.isfile(filePath)
if file:
    #Read information from file
    rfile = open(filePath, "rt")
    rfile.readline() #Read first line which is titles
    #Read all lines
    rows = rfile.readlines()
    #Run each line
    for row in rows:
        rData = row.split(",")
        if rData[1] not in ids:
            ids.add(rData[1])
    #Close read file
    rfile.close()


'''
    Get house listings data from web
    If the data not exist in the file, it will be write to the File

    Mississauga Link (Modify number 1 part)
    link = "https://listing.ca/mls/?.x.........2..$"
'''
#Write information to file
wfile = open(filePath, "a")
#File titles (Only be execute once)
if not file:
    wfile.write("ID,Address,Street,Neighbourhood,City,Price,Bathroom,Bedroom,Link\n")

existCount = 0
#Iterate from page 1 to page 499
for pageIndex in range(1,500):
    if existCount > 20:
        break

    link = "https://listing.ca/mls/?.x........." + str(pageIndex) + "..$"

    #Delay a few seconds, which can avoid the ip be banned
    delay = random.random()*4
    print(str(pageIndex) + "\t" + str(delay))
    time.sleep(delay)

    #HTTP request
    response = requests.get(link)
    #Get HTML code
    html = BeautifulSoup(response.text, "html.parser")
    #Get class name is "lc" (house content in the list)
    houseListing = html.select(".lc")
    #If houseListing have data, it will get house list information
    if houseListing:
        #Iterate all house
        for house in houseListing:
            if existCount > 20:
                break
            #Get ID
            print(house.get("id"))
            id = house.get("id")

            sltDivs = house.select_one(".slt").find_all("div")
            #Get above information
            # print(sltDivs[0].find("a").get("href")) #link
            link = sltDivs[0].find("a").get("href")
            # print(sltDivs[0].find("a").getText()) #address
            address = sltDivs[0].find("a").getText()
            # print(sltDivs[1].getText()) #Price
            price = sltDivs[1].getText().replace(",", "").replace(" CAD", "")
            # print(sltDivs[2].getText()) #How many bathrooms?
            bathrooms = sltDivs[2].getText()
            # print(sltDivs[3].getText()) #How many bedrooms?
            bedrooms = sltDivs[3].getText()

            na2ParentDiv = house.select_one(".sl_loc").find("div")
            na2s = na2ParentDiv.select("na2")
            #First: City
            #Second: Neighbourhood
            #Third: Street
            for i in range(0,3):
                if na2s[i].get("id"):
                    sc = na2s[i].find_next_sibling("script")
                    scriptstr = str(sc)
                    startIndex = scriptstr.rindex(",")+2
                    endIndex = scriptstr.rindex("')<")
                    # print(scriptstr[startIndex:endIndex])
                    place = scriptstr[startIndex:endIndex]
                else:
                    # print(na2s[i].getText())
                    place = na2s[i].getText()

                if i == 0:
                    city = place
                elif i == 1:
                    neighbourhood = place
                elif i == 2:
                    street = place

            #If this id not in ids set, it will be append to the file; Otherwise, existCount add 1
            if id not in ids:
                rowData = today + "," + id + "," + address + "," + street + "," + neighbourhood + "," + city + "," + price + "," + bathrooms + "," + bedrooms + "," + link + "\n"
                # print(rowData)
                wfile.write(rowData)
            else:
                existCount += 1
    else:
        break

wfile.close()
