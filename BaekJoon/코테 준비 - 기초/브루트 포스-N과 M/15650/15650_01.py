from itertools import combinations

n, m = map(int, input().split())
nums = list(i for i in range(1, n+1))

for num in combinations(nums, m):
    print(*num)