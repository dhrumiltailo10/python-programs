# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# URL :  http://py4e-data.dr-chuck.net/comments_1712119.xml or http://py4e-data.dr-chuck.net/comments_42.xml
import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl
sum = 0

# #code to ignore SSL certificate errors(accessing HTTPS URLs)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('enter the URL:')
fname = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(fname.decode())  #make an element tree from the XML format after decoding the data from the URL
lst = tree.findall('comments/comment') #makes a list of all the <comment>(child node) under <comments>(parent tag/node)
for item in lst:    #iterating through every <comment> in the list
    s = item.find('count').text  #retrieving text from <count> node(in the string form)
    sum = sum + int(s)
print('the sum of counts is:', sum)