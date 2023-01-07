# to sent a GET request to a webpage and retrieve the data using urllib and find frequency of words
import urllib.request, urllib.parse, urllib.error
counts = dict()
fname = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fname:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(counts)