def NoC(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    
    memo[n] = NoC(n-1, memo) + NoC(n-2, memo) + NoC(n-3, memo)

    return memo[n]

T = int(input())

for i in range(T):
    n = int(input())
    print(NoC(n))