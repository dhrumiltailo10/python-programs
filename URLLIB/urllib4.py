#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
x = 0
# code to ignore SSL certificate errors(accessing HTTPS URLs)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1712117.html', context=ctx).read()   # another link http://py4e-data.dr-chuck.net/comments_42.html
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')          #make a list of all the span tags
for span in spans:
    x = int(span.contents[0]) + x    #retrieving the contents of span tag in the form of strings 
print(x)

