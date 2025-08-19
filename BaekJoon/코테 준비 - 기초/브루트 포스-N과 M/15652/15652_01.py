import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(i for i in range(1, n+1))

for pos in product(nums, repeat=m):
    flag = True
    for i in range(m-1):
        if pos[i] > pos[i+1]:
            flag = False
            break
    
    if flag:
        print(*pos)