def factorial(n):
    if n <= 1:
        return 1
    
    return n*factorial(n-1)

def solution(n):
    answer = 1
    i = 2

    while True:
        if factorial(i) > n:
            break
        answer = i
        i += 1
    
    return answer