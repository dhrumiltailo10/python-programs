# to read a file, find all the lines of a certain type, count them.
# then extract the floating point value from those lines and find their average 
fname = input("enter the file name:")  # file name is mbox-short.txt
f = open(fname)
count = 0
total = 0
for line in f:
    if line.startswith('X-DSPAM-Confidence:'):    # condition for finding the line starting with X-DSPAM-Confidence:
        count = count + 1
        spos = line.find("0")                     # find the index of the floating point number
        num = line[spos:]                         #slicing the string to obtain that number(which is still a string)
        total = total + float(num)
print("average spam confidence: ", total/count) 