def solution(a, b):
    '''길이가 같은 두 1차원 정수 배열 a, b,
    a와 b의 내적을 return'''

    return sum(list(a[i]*b[i] for i in range(len(a))))