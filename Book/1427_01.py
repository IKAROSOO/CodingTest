nums = list(input())

for i in range(len(nums)):
    Max = i
    for j in range(i+1, len(nums)):
        if nums[j] > nums[Max]:
            Max = j
    if nums[i] < nums[Max]:
        temp = nums[i]
        nums[i] = nums[Max]
        nums[Max] = temp

for i in range(len(nums)):
    print(nums[i])