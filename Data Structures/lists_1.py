# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
fname = open('romeo.txt')
#f = fname.readlines()
new = []
result = []
for line in fname:
    words = line.split() # splits each word from each line and make a separate list of each line
    #print(words)      #remove # on line 8 & 10 to understand the difference
    new.extend(words)  # make the list from 4 lists to 1 list
#print(new)
new.sort()
print(new)

# to remove duplicate words from above list 'new'
for word in new:
    if word not in result:
        result.append(word)
print(result)
