n = int(input())
nums = [int(input()) for i in range(n)]

result = [0 for i in range(n)]

for i in range(n):
    for num in range(1, nums[i]+1):
        result[i] += (nums[i]//num)*num

for i in range(n):
    print(result[i])

'''
시간 초과
'''