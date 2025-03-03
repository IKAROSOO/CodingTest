n, m = map(int, input().split())
num = list(map(int, input().split()))

result = []

for i in range(m):
    a, b = map(int, input().split())
    sum = 0

    while a != b+1:
        sum += num[a-1]
        a += 1
    
    result.append(sum)

for i in range(m):
    print(result[i])

'''
시간초과가 발생 -> 구간합으로 문제를 다시 풀어야 함
'''