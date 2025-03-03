N, M = map(int, input().split())

numbers = list(range(1, N+1))

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result

cnt = int(factorial(N)/factorial(N-M))

for i in range(cnt):
    