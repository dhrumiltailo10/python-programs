#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# links are  http://py4e-data.dr-chuck.net/comments_42.json &   http://py4e-data.dr-chuck.net/comments_1712120.json

import urllib.request, urllib.parse, urllib.error
import json
sum = 0
url = input('enter the url:')
handle = urllib.request.urlopen(url)
data = handle.read()

js = json.loads(data)

for item in js['comments']:  # iterating through every dictionary inside comments and extracting value of 'count'
    s = item['count']
    sum = sum + int(s)

print(sum)