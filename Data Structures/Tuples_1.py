# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fname = open('mbox-short.txt')
lst = list()
lst1 = list()
counts = dict()
for  line in fname:
    if not line.startswith('From '):  # looping through every line of the text file and find lines starting with 'From '
        continue
    words = line.split()
    lst.append(words[5])  # splitting the line into words, extracting the time(6th word) and appending it to an empty list lst
for word in lst:
    lst1.append(word[:2])  #slicing every element of the list and extracting first two characters in a new list lst1
for item in lst1:
    counts[item] = counts.get(item,0) + 1 # method to make a dictionary consisting of different times as key and its frequency as value
newtup = (sorted(counts.items()))  #sorting the tuples in ascending order according to key(time values)
for k,v in newtup:
    print(k,v)

