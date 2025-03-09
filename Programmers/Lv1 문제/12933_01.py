def solution(n):
    '''n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴'''

    answer = sorted(list(map(int, str(n))), reverse=True)
    res = 0

    for num in answer:
        res = res*10 + num
    
    return res