# Phone-Number-Tracker
A Phone Number Location Tracker implemented using python libraries like Folium, phonenumbers &amp; OpenCage Geocoding API. 

# Libraries used :
1. phonenumbers
2. Folium

# APIs used :
OpenCage Geocoding

# Generating API Key :
API Key is generated from - https://opencagedata.com

# Finding the location of input phone number :
1. Accessing phone numbers using phonenumbers.parse() function  
2. Displaying location using geocoder.description_for_number() function

# Finding service provider :
Using carrier.name_for_number() function

# Finding latitude and longitude on map : 
Using OpenCageGeocode(Key) and explicitly defining latitude and longitude of the phone number

# Finding map location and plotting the map in HTML file :
1. Map location is determined using folium.Map() function
2. Map is saved with .html extension

# Map :
United Kingdom                    (Location)  
Tismi                             (Service Provider)  
54.7023545 -3.2765753             (Latitude, Longitude)
![Screenshot (750)](https://user-images.githubusercontent.com/86195118/126360798-6414acdb-0123-4527-acd6-5fcb4d7324bd.png)

India                             (Location)  
Idea                              (Service Provider)  
22.3511148 78.6677428             (Latitude, Longitude)  
![Screenshot (751)](https://user-images.githubusercontent.com/86195118/126361038-03b5db66-d2d6-41fa-8ec3-307bebe4ff4d.png)

Pennsylvania                      (Location)  
40.9699889 -77.7278831            (Latitude, Longitude)  
![Screenshot (754)](https://user-images.githubusercontent.com/86195118/126361133-9214a79c-f5a7-4143-b068-fe811e22baeb.png)
