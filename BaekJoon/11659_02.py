n, m = map(int, input().split())
num = list(map(int, input().split()))

num_sum = [0]
result = []
temp = 0

for i in num:
    temp += i
    num_sum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    result.append(num_sum[b] - num_sum[a-1])

for i in range(m):
    print(result[i])