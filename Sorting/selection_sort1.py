array = []

for i in range(1,6):
    array.append(int(input('enter array : ')))

print("start : ", array)

for i in range(0, len(array)):
    min_itm = array[i]
    min_idx = i

    for j in range(i+1, len(array)):
        if array[j] < min_itm :      
            min_itm = array[j]
            min_idx = j
            
    tmp = array[i]
    array[i] = array[min_idx]
    array[min_idx] = tmp
    print("step : ", array)

print("sorted array : ", array)