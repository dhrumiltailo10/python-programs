
s ="GEEKSFORGEEKS"

li = []
for i in range (0,len(s)):
    li.append(s[i])

for i in range(0, len(li)):
    for j in range(0, len(li)):
        if li[i] < li[j]:
            li[i],li[j] = li[j],li[i]
 
x = ""
for i in range(0, len(li)):
   x = x + li[i]

print(x)