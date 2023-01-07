# to sent a GET request to an HTML webpage and retrieve the data using urllib
import urllib.request, urllib.parse, urllib.error
fname = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in fname:
    print(line.decode().strip())
