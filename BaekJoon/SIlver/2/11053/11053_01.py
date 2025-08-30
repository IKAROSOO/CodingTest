n = int(input())
A = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = j

print(dp)