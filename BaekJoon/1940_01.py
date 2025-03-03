N = int(input())
M = int(input())

num = list(map(int, input().split()))
num.sort()

left, right = 0, N-1

cnt = 0

while left < right:
    if num[left]+num[right] > M:
        right -= 1
    elif num[left]+num[right] < M:
        left += 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)