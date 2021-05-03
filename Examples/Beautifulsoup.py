#Import Python Requests Package
import requests
#Import Python BeautifulSoup Package
from bs4 import BeautifulSoup

#Test HTTP Request
response = requests.get("https://www.google.com/")

#If success, it will print <Response [200]>
# print(response)

#Use BeautifulSoup to parse html code
soup = BeautifulSoup(response.text, "html.parser")

#Print out HTML code
# print(soup.prettify())

#================= Get some parts of HTML =================
#Get element by HTML Tag Name (Single)
htmlTagForm = soup.find("form")
# print(htmlTagForm)

#Get elements by HTML Tag Name (Multiple)
htmlTagInputs =  soup.find_all("input")
# print(htmlTagInputs)

#Get elements by HTML Tag Names and limit amount of number
htmlTagImgAndP = soup.find_all(["img", "p"], limit=2)
# print(htmlTagImgAndP)



#Use select_one function to get html tag (Single)
selectHtmlTagA = soup.select_one("a")
# print(selectHtmlTagA)

#Use select function to get html tags (Multiple)
selectHtmlTagAs = soup.select("a")
# print(selectHtmlTagAs)



#Use find to get CSS Attribute (Single)
classFindA = soup.find("a", class_="gb4")
# print(classFindA)

#Use find to get CSS Attribute (Multiple)
classFindAs = soup.find_all("a", class_="gb4")
# print(classFindAs)

#Use select to get CSS Attribute (Multiple)
classSelectAs = soup.select(".gb4")
# print(classSelectAs)



#================= Get Parent & front/back =================
#Get parents tags
getHtmlBTag = soup.find("b")
parents = getHtmlBTag.find_parents("nobr")
# print(parents)

#Get front tags (Must same level) (Multiple)
previousTags = getHtmlBTag.find_previous_siblings("div")
# print(previousTags)

#Get back tags (Must same level) (Multiple)
nextTags = getHtmlBTag.find_next_siblings("a");
# print(nextTags)

#Get front tags (Must same level) (Single)
previousTags = getHtmlBTag.find_previous_sibling("div")
# print(previousTags)

#Get back tags (Must same level) (Single)
nextTags = getHtmlBTag.find_next_sibling("a");
# print(nextTags)



#================= Get Attribute/Text Value =================
#Get attibute value
getAllAs = soup.find_all("a")
# for link in getAllAs:
#     print(link.get("href"))

#Get text value
for link in getAllAs:
    print(link.getText())
