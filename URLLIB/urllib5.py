#In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
i = 0
c = int(input('enter the count: '))   # number of times the program will run
p = int(input('enter the position:'))  # the position(relative to the first position) of the link which the program will keep on following

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/known_by_Ibrahim.html').read()  #alternate link http://py4e-data.dr-chuck.net/known_by_Fikret.html
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
print(tags[p-1].get('href', None)) # printing the URL at the user-defined position after following the above link

while i < (c-1):  # loop will run one less time as one URL is already printed when first link was followed
    x = urllib.request.urlopen(tags[p-1].get('href',None)).read()  # follow the link and read the URL at the user-defined position
    s = BeautifulSoup(x,'html.parser')  # parsing the html page using bs4
    tags = s('a')  # extracting all the anchor tags and storing them in a list
    i = i + 1
    print(tags[p-1].get('href', None)) # printing the URL at the user-defined position after following the above link





def new():
    i=0
    link = 'http://py4e-data.dr-chuck.net/known_by_Ibrahim.html';

    while i <= (c-1):  # loop will run one less time as one URL is already printed when first link was followed
        html = urllib.request.urlopen(link).read()  #alternate link http://py4e-data.dr-chuck.net/known_by_Fikret.html
        soup = BeautifulSoup(html,'html.parser')

        tags = soup('a')
        link = tags[p-1].get('href', None)
        print(link)
        i=i+1
        # printing the URL at the user-defined position after following the above link

new()

def withRecursion(c, p, link):
    html = urllib.request.urlopen(link).read()  #alternate link http://py4e-data.dr-chuck.net/known_by_Fikret.html
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('a')
    link = tags[p-1].get('href', None)
    print(link)
    if c<=0:
        return
    withRecursion(c-1, p, link)

withRecursion(c-1, p, 'http://py4e-data.dr-chuck.net/known_by_Ibrahim.html')