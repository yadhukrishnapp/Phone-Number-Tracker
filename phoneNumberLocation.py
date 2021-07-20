# pip install phonenumbers
# pip install folium
from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier
from phonenumbers import geocoder
import phonenumbers
import folium

from myNumber import numbers

Key = '4ff8eb5d8b9d429392b550e457e81aad'

# program to find the location of input phone number

phoneNumber = phonenumbers.parse(numbers[0]) # for accessing other numbers provided inside myNumber.py change the index value --> try numbers[1], numbers[2]

yourLocation = geocoder.description_for_number(phoneNumber, "en")
print(yourLocation)

# program to find the service provider

serviceProvider = phonenumbers.parse(numbers[0])
print(carrier.name_for_number(serviceProvider, "en"))

# program to get the latitude and longitude on map

# pip install opencage
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']  # Latitude of the phone number
lng = results[0]['geometry']['lng']  # Longitude of the phone number
print(lat, lng)

# program to get the map location

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

# plotting map in HTML file

myMap.save("Phone Number Tracker.html")
