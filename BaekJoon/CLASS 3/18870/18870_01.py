import sys

input = sys.stdin.readline

n = int(input())
tmp = list(map(int, input().split()))
nums = list()
answer = list()

for i in range(n):
    nums.append((tmp[i], i))

nums.sort()

cnt = -1
current = min(nums)

for num, index in nums:
    if current == num:
        answer.append((cnt, index))
        continue
    
    cnt += 1
    answer.append((cnt, index))

    current = num

ans = sorted(answer, key=lambda x:x[1])

for num in ans:
    print(num[0], end=" ")