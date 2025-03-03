T = int(input())
calender = []

for _ in range(T):
    data = list(map(int, input().split()))
    calender.append(data)

for datas in calender:
    M, N, x, y = datas
    found = False

    year = x
    while year < M * N:
        if (year - 1) % N == y - 1:
            print(year)
            found = True
            break
        year += M
    
    if not found:
        print(-1)