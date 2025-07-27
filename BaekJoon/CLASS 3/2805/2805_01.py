import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0

left, right = 0, max(trees)

while left <= right:
    mid = (left+right)//2
    
    cnt = sum(tree-mid for tree in trees if tree >= mid)

    if cnt >= m:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)