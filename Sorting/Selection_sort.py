f = open('hello.txt', 'r')
x = f.readline()
f.close()

inp_list = x.split(", ")  

nums = []
for i in inp_list:
    nums.append(int(i))

print("Start: ", nums)

for i in range(0, len(nums)):
    min_itm = nums[i]
    min_idx = i

    for j in range(i + 1, len(nums)):
        if nums[j] < min_itm:       # for descending change the sign to >
            min_itm = nums[j]
            min_idx = j

    tmp = nums[i]
    nums[i] = nums[min_idx]
    nums[min_idx] = tmp
    print("Step : ", nums)


print("Sorted: ", nums)