# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

fname = open('mbox-short.txt')
counts = {}
email = []

for line in fname:       # looping through every line of the text file and find lines starting with 'From '
    if not line.startswith('From '):
        continue
    words = line.split()
    email.append(words[1])   # splitting the line into words, extracting the the email address(2nd word) and appending it to an empty list email
for word in email:
    counts[word] = counts.get(word,0) + 1  # method to make a dictionary consisting of different emails as key and its frequency as value
name = None
frequency  = None
for key,value in counts.items():   # method to scan through list of items(list of key-value pair tuples ) and find key with maximum value
    if name is None or value > frequency:
        name = key
        frequency = value
print(name,frequency)