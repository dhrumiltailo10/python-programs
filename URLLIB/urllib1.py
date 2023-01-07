# to sent a GET request to a webpage and retrieve the data using urllib
#URL : http://data.pr4e.org/romeo.txt
import urllib.request, urllib.parse, urllib.error     #importing urllib libraries

fname = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  #this is equivalent to creating a socket, establish connection to web server & make a GET request all in one 

for line in fname:             #looping through the handle
    print(line.decode().strip())   #printing the data after decoding it(converting bytes strings to unicode)
    