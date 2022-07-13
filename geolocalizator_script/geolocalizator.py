from geopy.geocoders import Nominatim 
geolocator = Nominatim(user_agent="geopy.geocoder.GoogleV3")
location = geolocator.reverse("19.2824303, -99.2085626")
print(location.raw)