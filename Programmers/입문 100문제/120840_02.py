def solution(balls, share):
    answer = 0

    answer = comb(balls, share)

    return answer

def comb(n, m):
    if m > n-m:
        m = n-m

    result = 1
    for i in range(m):
        result *= (n-i)
        result //= (i+1)
    
    return result