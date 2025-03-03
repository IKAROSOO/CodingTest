def solution(balls, share):
    answer = 0

    upper = factorial(balls)
    downer = factorial(share) * factorial(balls-share)

    answer = upper/downer

    return answer

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
# 코드 상으로는 문제가 없지만, 런타임 에러가 발생한다.