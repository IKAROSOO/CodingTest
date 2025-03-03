def solution(n):
    array = []

    for i in range(n):
        if (2*i + 1) <= n:
            array.append(2*i + 1)
    
    return array