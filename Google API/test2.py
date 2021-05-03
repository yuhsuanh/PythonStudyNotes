import googlemaps
import pandas as pd
import time

gmaps = googlemaps.Client(key='AIzaSyC7lSKqhxhVwRAWY-SMJCStIsh2mrbxKKc')

cities=["Niagara Fall"]

ids = []
for city in cities:
	results = []
	# Geocoding an address
	geocode_result = gmaps.geocode(city)
	loc = geocode_result[0]['geometry']['location']
	query_result = gmaps.places_nearby(keyword="寵物",location=loc, radius=10000)
	results.extend(query_result['results'])

	while query_result.get('next_page_token'):
		time.sleep(2)
		query_result = gmaps.places_nearby(page_token=query_result['next_page_token'])
		results.extend(query_result['results'])    
	print("找到以"+city+"為中心半徑10000公尺的寵物店家數量(google mapi api上限提供60間): "+str(len(results)))

	for place in results:
		ids.append(place['place_id'])


stores_info = []
# 去除重複id
ids = list(set(ids)) 
for id in ids:
	stores_info.append(gmaps.place(place_id=id, language='en')['result'])

output = pd.DataFrame.from_dict(stores_info)
print(output)

df = pd.DataFrame(output)
df.to_csv("test_data1.csv")