#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
#To complete this assignment, you should use this API endpoint that has a static subset of the Google Data: http://py4e-data.dr-chuck.net/json?
#This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
#To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py
import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('eneter the location:')
params = {'key' : 42, 'address': address}
url = serviceurl + urllib.parse.urlencode(params)
print(url)

uh = urllib.request.urlopen(url)
data = uh.read().decode('utf-8')
js = json.loads(data)
print(json.dumps(js, indent=4))
print('Place id', js['results'][0]['place_id'])