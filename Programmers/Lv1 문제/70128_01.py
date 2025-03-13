def solution(a, b):
    '''길이가 같은 두 1차원 정수 배열 a, b,
    a와 b의 내적을 return'''

    answer = 0

    for i in range(len(a)):
        answer += a[i]*b[i]
    
    return answer