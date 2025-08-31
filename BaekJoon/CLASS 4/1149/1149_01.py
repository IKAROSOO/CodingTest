n = int(input())
costs = list()
dp = [[0] * 3 for _ in range(n)]

for _ in range(n):
    cost = list(map(int, input().split()))
    costs.append(cost)

dp[0] = costs[0]

for i in range(1, n):
    dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = costs[i][2] + min(dp[i-1][1], dp[i-1][0])

print(min(dp[n-1]))

'''
2025_08_31_20:03
다시 풀어볼 필요 있음
'''