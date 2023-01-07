# reading a file
f = open('hi.dat', 'r')
x = f.readline()
f.close()

# converting the data in the file from string to int and appending them to a list
y = x.split(",")
inp_lst = []
for i in y:
    inp_lst.append(int(i))

print("Initial order of numbers :", inp_lst)

# algorithm for sorting the list in ascending order
for i in range(0, len(inp_lst)):
    min_itm = inp_lst[i]
    min_idx = i

    for j in range(i+1, len(inp_lst)):
        if inp_lst[j] < min_itm:
            min_itm = inp_lst[j]
            min_idx = j
    tmp = inp_lst[i]
    inp_lst[i] = inp_lst[min_idx]
    inp_lst[min_idx] = tmp
print("Ascending order :", inp_lst)

# algorithm for sorting the list in descending order 
for i in range(0, len(inp_lst)):
    min_itm = inp_lst[i]
    min_idx = i

    for j in range(i+1, len(inp_lst)):
        if inp_lst[j] > min_itm:
            min_itm = inp_lst[j]
            min_idx = j
    tmp = inp_lst[i]
    inp_lst[i] = inp_lst[min_idx]
    inp_lst[min_idx] = tmp
print("Descending order :", inp_lst)