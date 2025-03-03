N, M = map(int, input().split())

a = []
b = []

for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    b.append(list(map(int, input().split())))

sum = []

for i in range(N):
    row = []
    for j in range(M):
        row.append(a[i][j] + b[i][j])

    sum.append(row)

for row in sum:
    print(' '.join(map(str, row)))