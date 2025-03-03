def NoC(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    cnt = 0

    if n > 3:
        cnt += NoC(n-3) + NoC(n-2) +NoC(n-1)
    
    return cnt

T = int(input())

for i in range(T):
    n = int(input())
    print(NoC(n))