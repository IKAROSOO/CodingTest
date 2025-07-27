import sys

input = sys.stdin.readline

k, n = map(int, input().split())
cables = list()

for _ in range(k):
    cables.append(int(input()))

right = max(cables)
left = 1
answer = 0

while left <= right:
    mid = (left+right)//2
    cnt = 0

    for cable in cables:
        cnt += cable//mid
    
    if cnt < n:
        right = mid-1
    else:
        left = mid+1
        answer = mid

print(answer)