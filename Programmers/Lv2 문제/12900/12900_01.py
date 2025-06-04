def solution(n):
    cnt = 0

    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    cnt += solution(n-2) + solution(n-1)

    return cnt

'''
방법적으로나 논리적으로는 맞는 방법
하지만 시간복잡도가 너무 크기 때문엘 좋지 않다.
'''