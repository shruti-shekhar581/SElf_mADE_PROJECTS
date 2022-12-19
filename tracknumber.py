import location as location
import phonenumbers

import opencage
import folium
from test import number
from phonenumbers import geocoder
pepnum=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnum,"en")
print(location)
from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))
from opencage.geocoder import OpenCageGeocode
key = "c66abed23f4a42bf8088b5d7b6ba8afb"
geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)
myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("my-location.html")