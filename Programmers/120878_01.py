def solution(a, b):
    answer = 0

    denominator = b / GCD(a, b)
    
    while denominator%2 == 0:
        denominator //= 2
    while denominator%5 == 0:
        denominator //= 5
    
    if denominator == 1:
        return 1
    else:
        return 2

def GCD(a, b):
    while b:
        a, b = b, a%b
    
    return a