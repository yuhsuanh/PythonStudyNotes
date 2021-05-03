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

	file = os.path.isfile(filePath)

	wfile = open(filePath, "a")
	if not file:
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


clinicsArray = []
#Blood Donor Clinics
bloodDonorClinicsUri = 'listservices.aspx?id=10181'
clinicsArray.append(bloodDonorClinicsUri)
#Blood Pressure Clinics
bloodPressureClinicsUri = 'listservices.aspx?id=10688'
clinicsArray.append(bloodPressureClinicsUri)
#Cancer Treatment Centres
cancerTreatmentCentresUri = 'listservices.aspx?id=10314'
clinicsArray.append(cancerTreatmentCentresUri)
#Complex Continuing Care
complexContinuingCareUri = 'listservices.aspx?id=11048'
clinicsArray.append(complexContinuingCareUri)
#Dental Clinics
dentalClinicsUri = 'listservices.aspx?id=10076'
clinicsArray.append(dentalClinicsUri)
#Diagnostic Imaging Clinics
diagnosticImagingClinicsUri = 'listservices.aspx?id=10629'
clinicsArray.append(diagnosticImagingClinicsUri)
#Emergency Departments
emergencyDepartmentsUri = 'listservices.aspx?id=10077'
clinicsArray.append(emergencyDepartmentsUri)
#Family Health Teams
familyHealthTeamsUri = 'listservices.aspx?id=10655'
clinicsArray.append(familyHealthTeamsUri)
#Family Medical Centres
familyMedicalCentresUri = 'listservices.aspx?id=10075'
clinicsArray.append(familyMedicalCentresUri)
#Foot Care - Clinics
footCareClinicsUri = 'listservices.aspx?id=10616'
clinicsArray.append(footCareClinicsUri)
#Immunization Clinics
immunizationClinicsUri = 'listservices.aspx?id=10079'
clinicsArray.append(immunizationClinicsUri)
#Long-Term Care
longtermCareUri = 'listservices.aspx?id=10665'
clinicsArray.append(longtermCareUri)
#Medical Laboratories
medicalLaboratoriesUri = 'listservices.aspx?id=10081'
clinicsArray.append(medicalLaboratoriesUri)
#Nursing Clinics
nursingClinicsUri = 'listservices.aspx?id=11228'
clinicsArray.append(nursingClinicsUri)
#Physiotherapy Services
physiotherapyServicesUri = 'listservices.aspx?id=11019'
clinicsArray.append(physiotherapyServicesUri)
#Rehabilitative Care
rehabilitativeCareUri = 'listservices.aspx?id=10827'
clinicsArray.append(rehabilitativeCareUri)
#Sport Medicine Clinics
sportMedicineClinicsUri = 'listservices.aspx?id=10284'
clinicsArray.append(sportMedicineClinicsUri)
#Women's Health Care Centres
womensHealthCareCentresUri = 'listservices.aspx?id=10145'
clinicsArray.append(womensHealthCareCentresUri)

for clinicUri in clinicsArray:
	# --- 1. Erie St. Clair Area ---
	print("1. Erie St. Clair Area")
	eriestclairhealthline = 'https://www.eriestclairhealthline.ca/'
	eriestclairFile = '1. Erie St. Clair Area.csv'
	getAreaClinics(eriestclairhealthline, clinicUri, eriestclairFile)

	# --- 2. South West Area ---
	print('2. South West Area')
	southwesthealthline = 'https://www.southwesthealthline.ca/'
	southwestFile = '2. South West Area.csv'
	getAreaClinics(southwesthealthline, clinicUri, southwestFile)

	# --- 3. Waterloo Wellington Area ---
	print('3. Waterloo Wellington Area')
	wwhealthline = 'https://www.wwhealthline.ca/'
	wwFile = '3. Waterloo Wellington Area.csv'
	getAreaClinics(wwhealthline, clinicUri, wwFile)

	# --- 4. Hamilton Niagara Haldimand Brant Area ---
	print('4. Hamilton Niagara Haldimand Brant Area')
	hnhbhealthline = 'https://www.hnhbhealthline.ca/'
	hnhbFile = '4. Hamilton Niagara Haldimand Brant Area.csv'
	getAreaClinics(hnhbhealthline, clinicUri, hnhbFile)

	# --- 5. Central West Area ---
	print('5. Central West Area')
	centralwesthealthline = 'https://www.centralwesthealthline.ca/'
	centralwestFile = '5. Central West Area.csv'
	getAreaClinics(centralwesthealthline, clinicUri, centralwestFile)

	# --- 6. Mississauga Halton Area ---
	print('6. Mississauga Halton Area')
	mississaugahaltonhealthline = 'https://www.mississaugahaltonhealthline.ca/'
	mississaugahaltonFile = '6. Mississauga Halton Area.csv'
	getAreaClinics(mississaugahaltonhealthline, clinicUri, mississaugahaltonFile)

	# --- 7. Toronto Central Area --- 
	print('7. Toronto Central Area')
	torontocentralhealthline = 'https://www.torontocentralhealthline.ca/'
	torontocentralFile = '7. Toronto Central Area.csv'
	getAreaClinics(torontocentralhealthline, clinicUri, torontocentralFile)

	# --- 8. Central Area ---
	print('8. Central Area')
	centralhealthline = 'https://www.centralhealthline.ca/'
	centralFile = '8. Central Area.csv'
	getAreaClinics(centralhealthline, clinicUri, centralFile)

	# --- 9. Central East Area ---
	print('9. Central East Area')
	centraleasthealthline = 'https://www.centraleasthealthline.ca/'
	centraleastFile = '9. Central East Area.csv'
	getAreaClinics(centraleasthealthline, clinicUri, centraleastFile)

	# --- 10. South East Area ---
	print('10. South East Area')
	southeasthealthline = 'https://www.southeasthealthline.ca/'
	southeastFile = '10. South East Area.csv'
	getAreaClinics(southeasthealthline, clinicUri, southeastFile)

	# --- 11. Champlain Area ---
	print('11. Champlain Area')
	champlainhealthline = 'https://www.champlainhealthline.ca/'
	champlainFile = '11. Champlain Area.csv'
	getAreaClinics(champlainhealthline, clinicUri, champlainFile)

	# --- 12. North Simcoe Muskoka Area ---
	print('12. North Simcoe Muskoka Area')
	nsmhealthline = 'https://www.nsmhealthline.ca/'
	nsmFile = '12. North Simcoe Muskoka Area.csv'
	getAreaClinics(nsmhealthline, clinicUri, nsmFile)

	# --- 13. North East Area ---
	print('13. North East Area')
	northeasthealthline = 'https://www.northeasthealthline.ca/'
	northeastFile = '13. North East Area.csv'
	getAreaClinics(northeasthealthline, clinicUri, northeastFile)

	# --- 14. North West Area ---
	print('14. North West Area')
	northwesthealthline = 'https://www.northwesthealthline.ca/'
	northwestFile = '14. North West Area.csv'
	getAreaClinics(northwesthealthline, clinicUri, northwestFile)
