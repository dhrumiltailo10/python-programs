arr = [1,6,3,8,9,4,7,11,16]

def lin_srch(x):
    for i in arr:
        if arr[i] == x:
            return i
    return "not found"
print(lin_srch(8))

arr.sort()  # [1,3,4,6,7,8,9,11,16]

def binarySearch(x, low, high):
    if(low <= high):
        mid = (low + high)//2
        
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(x, mid+1, high)
        else: 
            return binarySearch(x, low, mid-1)
    return "Not Found"


print(binarySearch(8, 0, len(arr)))