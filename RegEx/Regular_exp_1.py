#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

import re
fname = open('regex_sum2.txt')  #you can also use the other text file regex_sum1.txt
num_list = list()
sum = 0
for line in fname:
    line = line.rstrip()
    text = re.findall('[0-9]+',line) #[0-9]+ searches every line of the txt file for one or more digits(greedily) and stores them(in the form of string) as list in text variable
    if len(text) == 0:                # here we are ignoring all the lines which dot have any numbers
        continue
    for i in range(0,len(text)):    # looping every item of the list and adding them after converting them into int
        sum = sum + int(text[i])
print(sum)