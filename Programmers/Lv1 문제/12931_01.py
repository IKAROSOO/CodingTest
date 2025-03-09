def solution(n):
    '''자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수'''

    res = 0

    for num in str(n):
        res += int(num)
    
    return res