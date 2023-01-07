file = open('hi.txt', 'r')
for line in file:
    for word in line.split():
        print(word)