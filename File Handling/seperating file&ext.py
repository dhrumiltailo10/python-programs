
file = input("enter the file name with extension: ")

x = file.split('.')

print("the file name is %s"%x[0])
print("the file extension is %s"%x[1])