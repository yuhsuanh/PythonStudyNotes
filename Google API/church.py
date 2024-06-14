import googlemaps
import pandas as pd
import time

gmaps = googlemaps.Client(key='AIzaSyC7lSKqhxhVwRAWY-SMJCStIsh2mrbxKKc')

# municipalities = ["Addington Highlands Ontario", "Adelaide-Metcalfe Ontario", "Adjala-Tosorontio Ontario", "Admaston/Bromley Ontario", "Ajax Ontario", "Alberton Ontario", "Alfred and Plantagenet Ontario", "Algonquin Highlands Ontario", "Alnwick/Haldimand Ontario", "Amaranth Ontario", "Amherstburg Ontario", "Armour Ontario", "Armstrong Ontario", "Arnprior Ontario", "Arran-Elderslie Ontario", "Ashfield-Colborne-Wawanosh Ontario", "Asphodel-Norwood Ontario", "Assiginack Ontario", "Athens Ontario", "Atikokan Ontario", "Augusta Ontario", "Aurora Ontario", "Aylmer Ontario", "Baldwin Ontario", "Bancroft Ontario", "Barrie Ontario", "Bayham Ontario", "Beckwith Ontario", "Belleville Ontario", "Billings Ontario", "Black River-Matheson Ontario", "Blandford-Blenheim Ontario", "Blind River Ontario", "Bluewater Ontario", "Bonfield Ontario", "Bonnechere Valley Ontario", "Bracebridge Ontario", "Bradford West Gwillimbury Ontario", "Brampton Ontario", "Brant Ontario", "Brantford Ontario", "Brethour Ontario", "Brighton Ontario", "Brock Ontario", "Brockton Ontario", "Brockville Ontario", "Brooke-Alvinston Ontario", "Bruce Ontario", "Bruce Mines Ontario", "Brudenell Ontario", "Burk's Falls Ontario", "Burlington Ontario", "Burpee and Mills Ontario", "Caledon Ontario", "Callander Ontario", "Calvin Ontario", "Cambridge Ontario", "Carleton Place Ontario", "Carling Ontario", "Carlow/Mayo Ontario", "Casey Ontario", "Casselman Ontario", "Cavan Monaghan Ontario", "Central Elgin Ontario", "Central Frontenac Ontario", "Central Huron Ontario", "Central Manitoulin Ontario", "Centre Hastings Ontario", "Centre Wellington Ontario", "Chamberlain Ontario", "Champlain Ontario", "Chapleau Ontario", "Chapple Ontario", "Charlton and Dack Ontario", "Chatham-Kent Ontario", "Chatsworth Ontario", "Chisholm Ontario", "Clarence-Rockland Ontario", "Clarington Ontario", "Clearview Ontario", "Cobalt Ontario", "Cobourg Ontario", "Cochrane Ontario", "Cockburn Island Ontario", "Coleman Ontario", "Collingwood Ontario", "Conmee Ontario", "Cornwall Ontario", "Cramahe Ontario", "Dawn-Euphemia Ontario", "Dawson Ontario", "Deep River Ontario", "Deseronto Ontario", "Dorion Ontario", "Douro-Dummer Ontario", "Drummond/North Elmsley Ontario", "Dryden Ontario", "Dubreuilville Ontario", "Dufferin Ontario", "Durham Ontario", "Dutton/Dunwich Ontario", "Dysart et al Ontario", "Ear Falls Ontario", "East Ferris Ontario", "East Garafraxa Ontario", "East Gwillimbury Ontario", "East Hawkesbury Ontario", "East Zorra-Tavistock Ontario", "Edwardsburgh/Cardinal Ontario", "Elgin Ontario", "Elizabethtown-Kitley Ontario", "Elliot Lake Ontario", "Emo Ontario", "Englehart Ontario", "Enniskillen Ontario", "Erin Ontario", "Espanola Ontario", "Essa Ontario", "Essex Ontario", "Essex Ontario", "Evanturel Ontario", "Faraday Ontario", "Fauquier-Strickland Ontario", "Fort Erie Ontario", "Fort Frances Ontario", "French River Ontario", "Front of Yonge Ontario", "Frontenac Ontario", "Frontenac Islands Ontario", "Gananoque Ontario", "Gauthier Ontario", "Georgian Bay Ontario", "Georgian Bluffs Ontario", "Georgina Ontario", "Gillies Ontario", "Goderich Ontario", "Gordon/Barrie Island Ontario", "Gore Bay Ontario", "Grand Valley Ontario", "Gravenhurst Ontario", "Greater Madawaska Ontario", "Greater Napanee Ontario", "Greater Sudbury Ontario", "Greenstone Ontario", "Grey Ontario", "Grey Highlands Ontario", "Grimsby Ontario", "Guelph Ontario", "Guelph/Eramosa Ontario", "Haldimand County Ontario", "Haliburton Ontario", "Halton Ontario", "Halton Hills Ontario", "Hamilton Ontario", "Hamilton Ontario", "Hanover Ontario", "Harley Ontario", "Harris Ontario", "Hastings Ontario", "Hastings Highlands Ontario", "Havelock-Belmont-Methuen Ontario", "Hawkesbury Ontario", "Head Ontario", "Hearst Ontario", "Highlands East Ontario", "Hilliard Ontario", "Hilton Ontario", "Hilton Beach Ontario", "Hornepayne Ontario", "Horton Ontario", "Howick Ontario", "Hudson Ontario", "Huntsville Ontario", "Huron Ontario", "Huron East Ontario", "Huron Shores Ontario", "Huron-Kinloss Ontario", "Ignace Ontario", "Ingersoll Ontario", "Innisfil Ontario", "Iroquois Falls Ontario", "James Ontario", "Jocelyn Ontario", "Johnson Ontario", "Joly Ontario", "Kapuskasing Ontario", "Kawartha Lakes Ontario", "Kearney Ontario", "Kenora Ontario", "Kerns Ontario", "Killaloe Ontario", "Killarney Ontario", "Kincardine Ontario", "King Ontario", "Kingston Ontario", "Kingsville Ontario", "Kirkland Lake Ontario", "Kitchener Ontario", "La Vallee Ontario", "Laird Ontario", "Lake of Bays Ontario", "Lake of the Woods Ontario", "Lakeshore Ontario", "Lambton Ontario", "Lambton Shores Ontario", "Lanark Ontario", "Lanark Highlands Ontario", "Larder Lake Ontario", "LaSalle Ontario", "Latchford Ontario", "Laurentian Hills Ontario", "Laurentian Valley Ontario", "Leamington Ontario", "Leeds and Grenville Ontario", "Leeds and the Thousand Islands Ontario", "Lennox and Addington Ontario", "Limerick Ontario", "Lincoln Ontario", "London Ontario", "Loyalist Ontario", "Lucan Biddulph Ontario", "Macdonald Ontario", "Machar Ontario", "Machin Ontario", "Madawaska Valley Ontario", "Madoc Ontario", "Magnetawan Ontario", "Malahide Ontario", "Manitouwadge Ontario", "Mapleton Ontario", "Marathon Ontario", "Markham Ontario", "Markstay-Warren Ontario", "Marmora and Lake Ontario", "Matachewan Ontario", "Mattawa Ontario", "Mattawan Ontario", "Mattice-Val C??t?? Ontario", "McDougall Ontario", "McGarry Ontario", "McKellar Ontario", "McMurrich/Monteith Ontario", "McNab/Braeside Ontario", "Meaford Ontario", "Melancthon Ontario", "Merrickville-Wolford Ontario", "Middlesex Ontario", "Middlesex Centre Ontario", "Midland Ontario", "Milton Ontario", "Minden Hills Ontario", "Minto Ontario", "Mississauga Ontario", "Mississippi Mills Ontario", "Mono Ontario", "Montague Ontario", "Moonbeam Ontario", "Moosonee Ontario", "Morley Ontario", "Morris-Turnberry Ontario", "Mulmur Ontario", "Muskoka Ontario", "Muskoka Lakes Ontario", "Nairn and Hyman Ontario", "Neebing Ontario", "New Tecumseth Ontario", "Newbury Ontario", "Newmarket Ontario", "Niagara Ontario", "Niagara Falls Ontario", "Niagara-on-the-Lake Ontario", "Nipigon Ontario", "Nipissing Ontario", "Norfolk County Ontario", "North Algona Wilberforce Ontario", "North Bay Ontario", "North Dumfries Ontario", "North Dundas Ontario", "North Frontenac Ontario", "North Glengarry Ontario", "North Grenville Ontario", "North Huron Ontario", "North Kawartha Ontario", "North Middlesex Ontario", "North Perth Ontario", "North Stormont Ontario", "Northeastern Manitoulin and The Islands Ontario", "Northern Bruce Peninsula Ontario", "Northumberland Ontario", "Norwich Ontario", "Oakville Ontario", "O'Connor Ontario", "Oil Springs Ontario", "Oliver Paipoonge Ontario", "Opasatika Ontario", "Orangeville Ontario", "Orillia Ontario", "Oro-Medonte Ontario", "Oshawa Ontario", "Otonabee-South Monaghan Ontario", "Ottawa Ontario", "Owen Sound Ontario", "Oxford Ontario", "Papineau-Cameron Ontario", "Parry Sound Ontario", "Peel Ontario", "Pelee Ontario", "Pelham Ontario", "Pembroke Ontario", "Penetanguishene Ontario", "Perry Ontario", "Perth Ontario", "Perth Ontario", "Perth East Ontario", "Perth South Ontario", "Petawawa Ontario", "Peterborough Ontario", "Peterborough Ontario", "Petrolia Ontario", "Pickering Ontario", "Pickle Lake Ontario", "Plummer Additional Ontario", "Plympton-Wyoming Ontario", "Point Edward Ontario", "Port Colborne Ontario", "Port Hope Ontario", "Powassan Ontario", "Prescott Ontario", "Prescott and Russell Ontario", "Prince Ontario", "Prince Edward Ontario", "Puslinch Ontario", "Quinte West Ontario", "Rainy River Ontario", "Ramara Ontario", "Red Lake Ontario", "Red Rock Ontario", "Renfrew Ontario", "Renfrew Ontario", "Richmond Hill Ontario", "Rideau Lakes Ontario", "Russell Ontario", "Ryerson Ontario", "Sables-Spanish Rivers Ontario", "Sarnia Ontario", "Saugeen Shores Ontario", "Sault Ste. Marie Ontario", "Schreiber Ontario", "Scugog Ontario", "Seguin Ontario", "Selwyn Ontario", "Severn Ontario", "Shelburne Ontario", "Shuniah Ontario", "Simcoe Ontario", "Sioux Lookout Ontario", "Sioux Narrows-Nestor Falls Ontario", "Smiths Falls Ontario", "Smooth Rock Falls Ontario", "South Algonquin Ontario", "South Bruce Ontario", "South Bruce Peninsula Ontario", "South Dundas Ontario", "South Frontenac Ontario", "South Glengarry Ontario", "South Huron Ontario", "South River Ontario", "South Stormont Ontario", "Southgate Ontario", "Southwest Middlesex Ontario", "South-West Oxford Ontario", "Southwold Ontario", "Spanish Ontario", "Springwater Ontario", "St. Catharines Ontario", "St. Clair Ontario", "St. Joseph Ontario", "St. Marys Ontario", "St. Thomas Ontario", "St.-Charles Ontario", "Stirling-Rawdon Ontario", "Stone Mills Ontario", "Stormont Ontario", "Stratford Ontario", "Strathroy-Caradoc Ontario", "Strong Ontario", "Sundridge Ontario", "Tarbutt Ontario", "Tay Ontario", "Tay Valley Ontario", "Tecumseh Ontario", "Tehkummah Ontario", "Temagami Ontario", "Temiskaming Shores Ontario", "Terrace Bay Ontario", "Thames Centre Ontario", "The Archipelago Ontario", "The Blue Mountains Ontario", "The Nation Municipality Ontario", "The North Shore Ontario", "Thessalon Ontario", "Thornloe Ontario", "Thorold Ontario", "Thunder Bay Ontario", "Tillsonburg Ontario", "Timmins Ontario", "Tiny Ontario", "Toronto Ontario", "Trent Hills Ontario", "Trent Lakes Ontario", "Tudor and Cashel Ontario", "Tweed Ontario", "Tyendinaga Ontario", "Uxbridge Ontario", "Val Rita-Harty Ontario", "Vaughan Ontario", "Wainfleet Ontario", "Warwick Ontario", "Wasaga Beach Ontario", "Waterloo Ontario", "Wawa Ontario", "Welland Ontario", "Wellesley Ontario", "Wellington Ontario", "Wellington North Ontario", "West Elgin Ontario", "West Grey Ontario", "West Lincoln Ontario", "West Nipissing Ontario", "West Perth Ontario", "Westport Ontario", "Whitby Ontario", "Whitchurch-Stouffville Ontario", "White River Ontario", "Whitestone Ontario", "Whitewater Region Ontario", "Wilmot Ontario", "Windsor Ontario", "Wollaston Ontario", "Woodstock Ontario", "Woolwich Ontario", "York Ontario", "Zorra Ontario"]

# municipalities = ["Addington Highlands Ontario", "Adelaide-Metcalfe Ontario", "Adjala-Tosorontio Ontario", "Admaston/Bromley Ontario", "Ajax Ontario", "Alberton Ontario", "Alfred and Plantagenet Ontario", "Algonquin Highlands Ontario", "Alnwick/Haldimand Ontario", "Amaranth Ontario", "Amherstburg Ontario", "Armour Ontario", "Armstrong Ontario", "Arnprior Ontario", "Arran-Elderslie Ontario", "Ashfield-Colborne-Wawanosh Ontario", "Asphodel-Norwood Ontario", "Assiginack Ontario", "Athens Ontario", "Atikokan Ontario", "Augusta Ontario", "Aurora Ontario", "Aylmer Ontario", "Baldwin Ontario", "Bancroft Ontario", "Barrie Ontario", "Bayham Ontario", "Beckwith Ontario", "Belleville Ontario", "Billings Ontario", "Black River-Matheson Ontario", "Blandford-Blenheim Ontario", "Blind River Ontario", "Bluewater Ontario", "Bonfield Ontario", "Bonnechere Valley Ontario", "Bracebridge Ontario", "Bradford West Gwillimbury Ontario", "Brampton Ontario", "Brant Ontario", "Brantford Ontario", "Brethour Ontario", "Brighton Ontario", "Brock Ontario", "Brockton Ontario", "Brockville Ontario", "Brooke-Alvinston Ontario", "Bruce Ontario", "Bruce Mines Ontario", "Brudenell Ontario", "Burk's Falls Ontario", "Burlington Ontario", "Burpee and Mills Ontario", "Caledon Ontario", "Callander Ontario", "Calvin Ontario", "Cambridge Ontario", "Carleton Place Ontario", "Carling Ontario", "Carlow/Mayo Ontario", "Casey Ontario", "Casselman Ontario", "Cavan Monaghan Ontario", "Central Elgin Ontario", "Central Frontenac Ontario", "Central Huron Ontario", "Central Manitoulin Ontario", "Centre Hastings Ontario", "Centre Wellington Ontario", "Chamberlain Ontario", "Champlain Ontario", "Chapleau Ontario", "Chapple Ontario", "Charlton and Dack Ontario", "Chatham-Kent Ontario", "Chatsworth Ontario", "Chisholm Ontario", "Clarence-Rockland Ontario", "Clarington Ontario", "Clearview Ontario", "Cobalt Ontario", "Cobourg Ontario", "Cochrane Ontario", "Cockburn Island Ontario", "Coleman Ontario", "Collingwood Ontario", "Conmee Ontario", "Cornwall Ontario", "Cramahe Ontario", "Dawn-Euphemia Ontario", "Dawson Ontario", "Deep River Ontario", "Deseronto Ontario", "Dorion Ontario", "Douro-Dummer Ontario", "Drummond/North Elmsley Ontario", "Dryden Ontario", "Dubreuilville Ontario", "Dufferin Ontario", "Durham Ontario", "Dutton/Dunwich Ontario", "Dysart et al Ontario", "Ear Falls Ontario", "East Ferris Ontario", "East Garafraxa Ontario", "East Gwillimbury Ontario", "East Hawkesbury Ontario", "East Zorra-Tavistock Ontario", "Edwardsburgh/Cardinal Ontario", "Elgin Ontario", "Elizabethtown-Kitley Ontario", "Elliot Lake Ontario", "Emo Ontario", "Englehart Ontario", "Enniskillen Ontario", "Erin Ontario", "Espanola Ontario", "Essa Ontario", "Essex Ontario", "Essex Ontario", "Evanturel Ontario", "Faraday Ontario", "Fauquier-Strickland Ontario", "Fort Erie Ontario", "Fort Frances Ontario", "French River Ontario", "Front of Yonge Ontario", "Frontenac Ontario", "Frontenac Islands Ontario", "Gananoque Ontario", "Gauthier Ontario", "Georgian Bay Ontario", "Georgian Bluffs Ontario", "Georgina Ontario", "Gillies Ontario", "Goderich Ontario", "Gordon/Barrie Island Ontario", "Gore Bay Ontario", "Grand Valley Ontario", "Gravenhurst Ontario", "Greater Madawaska Ontario", "Greater Napanee Ontario", "Greater Sudbury Ontario", "Greenstone Ontario", "Grey Ontario", "Grey Highlands Ontario", "Grimsby Ontario", "Guelph Ontario", "Guelph/Eramosa Ontario"]
# municipalities = ["Haldimand County Ontario", "Haliburton Ontario", "Halton Ontario", "Halton Hills Ontario", "Hamilton Ontario", "Hamilton Ontario", "Hanover Ontario", "Harley Ontario", "Harris Ontario", "Hastings Ontario", "Hastings Highlands Ontario", "Havelock-Belmont-Methuen Ontario", "Hawkesbury Ontario", "Head Ontario", "Hearst Ontario", "Highlands East Ontario", "Hilliard Ontario", "Hilton Ontario", "Hilton Beach Ontario", "Hornepayne Ontario", "Horton Ontario", "Howick Ontario", "Hudson Ontario", "Huntsville Ontario", "Huron Ontario", "Huron East Ontario", "Huron Shores Ontario", "Huron-Kinloss Ontario", "Ignace Ontario", "Ingersoll Ontario", "Innisfil Ontario", "Iroquois Falls Ontario", "James Ontario", "Jocelyn Ontario", "Johnson Ontario", "Joly Ontario", "Kapuskasing Ontario", "Kawartha Lakes Ontario", "Kearney Ontario", "Kenora Ontario", "Kerns Ontario", "Killaloe Ontario", "Killarney Ontario", "Kincardine Ontario", "King Ontario", "Kingston Ontario", "Kingsville Ontario", "Kirkland Lake Ontario", "Kitchener Ontario", "La Vallee Ontario", "Laird Ontario", "Lake of Bays Ontario", "Lake of the Woods Ontario", "Lakeshore Ontario", "Lambton Ontario", "Lambton Shores Ontario", "Lanark Ontario", "Lanark Highlands Ontario", "Larder Lake Ontario", "LaSalle Ontario", "Latchford Ontario", "Laurentian Hills Ontario", "Laurentian Valley Ontario", "Leamington Ontario", "Leeds and Grenville Ontario", "Leeds and the Thousand Islands Ontario", "Lennox and Addington Ontario", "Limerick Ontario", "Lincoln Ontario", "London Ontario", "Loyalist Ontario", "Lucan Biddulph Ontario", "Macdonald Ontario", "Machar Ontario", "Machin Ontario", "Madawaska Valley Ontario", "Madoc Ontario", "Magnetawan Ontario", "Malahide Ontario", "Manitouwadge Ontario", "Mapleton Ontario", "Marathon Ontario", "Markham Ontario", "Markstay-Warren Ontario", "Marmora and Lake Ontario", "Matachewan Ontario", "Mattawa Ontario", "Mattawan Ontario", "Mattice-Val C??t?? Ontario", "McDougall Ontario", "McGarry Ontario", "McKellar Ontario", "McMurrich/Monteith Ontario", "McNab/Braeside Ontario", "Meaford Ontario", "Melancthon Ontario", "Merrickville-Wolford Ontario", "Middlesex Ontario", "Middlesex Centre Ontario", "Midland Ontario", "Milton Ontario", "Minden Hills Ontario", "Minto Ontario", "Mississauga Ontario", "Mississippi Mills Ontario", "Mono Ontario", "Montague Ontario", "Moonbeam Ontario", "Moosonee Ontario", "Morley Ontario", "Morris-Turnberry Ontario", "Mulmur Ontario", "Muskoka Ontario", "Muskoka Lakes Ontario", "Nairn and Hyman Ontario", "Neebing Ontario", "New Tecumseth Ontario", "Newbury Ontario", "Newmarket Ontario", "Niagara Ontario", "Niagara Falls Ontario", "Niagara-on-the-Lake Ontario", "Nipigon Ontario", "Nipissing Ontario", "Norfolk County Ontario", "North Algona Wilberforce Ontario", "North Bay Ontario", "North Dumfries Ontario", "North Dundas Ontario", "North Frontenac Ontario", "North Glengarry Ontario", "North Grenville Ontario", "North Huron Ontario", "North Kawartha Ontario", "North Middlesex Ontario", "North Perth Ontario", "North Stormont Ontario", "Northeastern Manitoulin and The Islands Ontario", "Northern Bruce Peninsula Ontario", "Northumberland Ontario", "Norwich Ontario", "Oakville Ontario", "O'Connor Ontario", "Oil Springs Ontario", "Oliver Paipoonge Ontario", "Opasatika Ontario", "Orangeville Ontario", "Orillia Ontario", "Oro-Medonte Ontario", "Oshawa Ontario", "Otonabee-South Monaghan Ontario", "Ottawa Ontario", "Owen Sound Ontario", "Oxford Ontario"]
# municipalities = ["Papineau-Cameron Ontario", "Parry Sound Ontario", "Peel Ontario", "Pelee Ontario", "Pelham Ontario", "Pembroke Ontario", "Penetanguishene Ontario", "Perry Ontario", "Perth Ontario", "Perth Ontario", "Perth East Ontario", "Perth South Ontario", "Petawawa Ontario", "Peterborough Ontario", "Peterborough Ontario", "Petrolia Ontario", "Pickering Ontario", "Pickle Lake Ontario", "Plummer Additional Ontario", "Plympton-Wyoming Ontario", "Point Edward Ontario", "Port Colborne Ontario", "Port Hope Ontario", "Powassan Ontario", "Prescott Ontario", "Prescott and Russell Ontario", "Prince Ontario", "Prince Edward Ontario", "Puslinch Ontario", "Quinte West Ontario", "Rainy River Ontario", "Ramara Ontario", "Red Lake Ontario", "Red Rock Ontario", "Renfrew Ontario", "Renfrew Ontario", "Richmond Hill Ontario", "Rideau Lakes Ontario", "Russell Ontario", "Ryerson Ontario", "Sables-Spanish Rivers Ontario", "Sarnia Ontario", "Saugeen Shores Ontario", "Sault Ste. Marie Ontario", "Schreiber Ontario", "Scugog Ontario", "Seguin Ontario", "Selwyn Ontario", "Severn Ontario", "Shelburne Ontario", "Shuniah Ontario", "Simcoe Ontario", "Sioux Lookout Ontario", "Sioux Narrows-Nestor Falls Ontario", "Smiths Falls Ontario", "Smooth Rock Falls Ontario", "South Algonquin Ontario", "South Bruce Ontario", "South Bruce Peninsula Ontario", "South Dundas Ontario", "South Frontenac Ontario", "South Glengarry Ontario", "South Huron Ontario", "South River Ontario", "South Stormont Ontario", "Southgate Ontario", "Southwest Middlesex Ontario", "South-West Oxford Ontario", "Southwold Ontario", "Spanish Ontario", "Springwater Ontario", "St. Catharines Ontario", "St. Clair Ontario", "St. Joseph Ontario", "St. Marys Ontario", "St. Thomas Ontario", "St.-Charles Ontario", "Stirling-Rawdon Ontario", "Stone Mills Ontario", "Stormont Ontario", "Stratford Ontario", "Strathroy-Caradoc Ontario", "Strong Ontario", "Sundridge Ontario", "Tarbutt Ontario", "Tay Ontario", "Tay Valley Ontario", "Tecumseh Ontario", "Tehkummah Ontario", "Temagami Ontario", "Temiskaming Shores Ontario", "Terrace Bay Ontario", "Thames Centre Ontario", "The Archipelago Ontario", "The Blue Mountains Ontario", "The Nation Municipality Ontario", "The North Shore Ontario", "Thessalon Ontario", "Thornloe Ontario", "Thorold Ontario", "Thunder Bay Ontario", "Tillsonburg Ontario", "Timmins Ontario", "Tiny Ontario", "Toronto Ontario", "Trent Hills Ontario", "Trent Lakes Ontario", "Tudor and Cashel Ontario", "Tweed Ontario", "Tyendinaga Ontario", "Uxbridge Ontario", "Val Rita-Harty Ontario", "Vaughan Ontario", "Wainfleet Ontario", "Warwick Ontario", "Wasaga Beach Ontario", "Waterloo Ontario", "Wawa Ontario", "Welland Ontario", "Wellesley Ontario", "Wellington Ontario", "Wellington North Ontario", "West Elgin Ontario", "West Grey Ontario", "West Lincoln Ontario", "West Nipissing Ontario", "West Perth Ontario", "Westport Ontario", "Whitby Ontario", "Whitchurch-Stouffville Ontario", "White River Ontario", "Whitestone Ontario", "Whitewater Region Ontario", "Wilmot Ontario", "Windsor Ontario", "Wollaston Ontario", "Woodstock Ontario", "Woolwich Ontario", "York Ontario", "Zorra Ontario"]

# municipalities = ["Haldimand County Ontario", "Haliburton Ontario", "Halton Ontario", "Halton Hills Ontario", "Hamilton Ontario", "Hamilton Ontario", "Hanover Ontario", "Harley Ontario", "Harris Ontario", "Hastings Ontario", "Hastings Highlands Ontario", "Havelock-Belmont-Methuen Ontario", "Hawkesbury Ontario", "Head Ontario", "Hearst Ontario", "Highlands East Ontario", "Hilliard Ontario", "Hilton Ontario", "Hilton Beach Ontario", "Hornepayne Ontario", "Horton Ontario", "Howick Ontario", "Hudson Ontario", "Huntsville Ontario", "Huron Ontario", "Huron East Ontario", "Huron Shores Ontario", "Huron-Kinloss Ontario", "Ignace Ontario", "Ingersoll Ontario", "Innisfil Ontario", "Iroquois Falls Ontario", "James Ontario", "Jocelyn Ontario", "Johnson Ontario", "Joly Ontario", "Kapuskasing Ontario", "Kawartha Lakes Ontario", "Kearney Ontario", "Kenora Ontario", "Kerns Ontario", "Killaloe Ontario", "Killarney Ontario", "Kincardine Ontario", "King Ontario", "Kingston Ontario", "Kingsville Ontario", "Kirkland Lake Ontario", "Kitchener Ontario", "La Vallee Ontario", "Laird Ontario", "Lake of Bays Ontario", "Lake of the Woods Ontario", "Lakeshore Ontario", "Lambton Ontario", "Lambton Shores Ontario", "Lanark Ontario", "Lanark Highlands Ontario", "Larder Lake Ontario", "LaSalle Ontario", "Latchford Ontario", "Laurentian Hills Ontario", "Laurentian Valley Ontario", "Leamington Ontario", "Leeds and Grenville Ontario", "Leeds and the Thousand Islands Ontario", "Lennox and Addington Ontario", "Limerick Ontario", "Lincoln Ontario", "London Ontario", "Loyalist Ontario", "Lucan Biddulph Ontario", "Macdonald Ontario", "Machar Ontario", "Machin Ontario", "Madawaska Valley Ontario", "Madoc Ontario"]
# municipalities = ["Magnetawan Ontario", "Malahide Ontario", "Manitouwadge Ontario", "Mapleton Ontario", "Marathon Ontario", "Markham Ontario", "Markstay-Warren Ontario", "Marmora and Lake Ontario", "Matachewan Ontario", "Mattawa Ontario", "Mattawan Ontario", "Mattice-Val C??t?? Ontario", "McDougall Ontario", "McGarry Ontario", "McKellar Ontario", "McMurrich/Monteith Ontario", "McNab/Braeside Ontario", "Meaford Ontario", "Melancthon Ontario", "Merrickville-Wolford Ontario", "Middlesex Ontario", "Middlesex Centre Ontario", "Midland Ontario", "Milton Ontario", "Minden Hills Ontario", "Minto Ontario", "Mississauga Ontario", "Mississippi Mills Ontario", "Mono Ontario", "Montague Ontario", "Moonbeam Ontario", "Moosonee Ontario", "Morley Ontario", "Morris-Turnberry Ontario", "Mulmur Ontario", "Muskoka Ontario", "Muskoka Lakes Ontario"]
municipalities = ["Nairn and Hyman Ontario", "Neebing Ontario", "New Tecumseth Ontario", "Newbury Ontario", "Newmarket Ontario", "Niagara Ontario", "Niagara Falls Ontario", "Niagara-on-the-Lake Ontario", "Nipigon Ontario", "Nipissing Ontario", "Norfolk County Ontario", "North Algona Wilberforce Ontario", "North Bay Ontario", "North Dumfries Ontario", "North Dundas Ontario", "North Frontenac Ontario", "North Glengarry Ontario", "North Grenville Ontario", "North Huron Ontario", "North Kawartha Ontario", "North Middlesex Ontario", "North Perth Ontario", "North Stormont Ontario", "Northeastern Manitoulin and The Islands Ontario", "Northern Bruce Peninsula Ontario", "Northumberland Ontario", "Norwich Ontario", "Oakville Ontario", "O'Connor Ontario", "Oil Springs Ontario", "Oliver Paipoonge Ontario", "Opasatika Ontario", "Orangeville Ontario", "Orillia Ontario", "Oro-Medonte Ontario", "Oshawa Ontario", "Otonabee-South Monaghan Ontario", "Ottawa Ontario", "Owen Sound Ontario", "Oxford Ontario"]

ids = []
for municipality in municipalities:
	results = []
	# Geocoding an address
	geocode_result = gmaps.geocode(municipality)
	loc = geocode_result[0]['geometry']['location']
	query_result = gmaps.places_nearby(keyword="Church",location=loc, radius=10000)
	results.extend(query_result['results'])

	while query_result.get('next_page_token'):
		time.sleep(2)
		query_result = gmaps.places_nearby(page_token=query_result['next_page_token'])
		results.extend(query_result['results'])    
	print("Found \'Churches\' around \""+municipality+"\" circle 10000 meters (google mapi api max 60 places): "+str(len(results)))

	for place in results:
		ids.append(place['place_id'])

stores_info = []
# Remove duplicate data
ids = list(set(ids)) 
for id in ids:
	stores_info.append(gmaps.place(place_id=id, language='en')['result'])

output = pd.DataFrame.from_dict(stores_info)
print(output)

df = pd.DataFrame(output)
df.to_csv("churches_info2-3.csv")