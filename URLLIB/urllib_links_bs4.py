# using beautiful soup to parse HTML webpages(both HTTP & HTTPS) and retrieving all the links on that webpage
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# code to ignore SSL certificate errors(accessing HTTPS URLs)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("enter a URL : ")   #asking user for a URL
html = urllib.request.urlopen(url, context=ctx).read()  #accessing the URL and reading it
soup = BeautifulSoup(html, 'html.parser')  # using beautiful soup to parse the html and store it in soup variable

# to retrieve all the links
tags = soup('a')    # makes a list of all the anchor tags in the parsed html document (soup in this case) 
for tag in tags:
    print(tag.get('href', None))   #for every anchor tag, retrieve the value(link) for href key and print it
   

#for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)