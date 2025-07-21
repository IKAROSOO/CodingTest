n = int(input())
nums = list(map(int, input().split()))

nums.sort()

cnt = 0
i = 1

while i < n+1:
    for k in range(i):
        cnt += nums[k]
    
    i += 1

print(cnt)