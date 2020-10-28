#Import Python Requests Package
import requests

#Test HTTP Request
response = requests.get("https://www.google.com/")

#If success, it will print <Response [200]>
print(response)
