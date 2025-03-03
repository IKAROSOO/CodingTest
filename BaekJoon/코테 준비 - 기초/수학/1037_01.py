n = int(input())
nums = list(map(int, input().split()))

nums.sort()

if n%2 != 0:
    middle_index = int(n/2)
    print(nums[middle_index]**2)
else:
    print(nums[0]*nums[-1])