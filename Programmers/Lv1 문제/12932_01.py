def solution(n):
    '''자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴'''

    answer = []

    for i in range(len(str(n))):
        answer.append(int(str(n)[len(str(n)) - i - 1]))
    
    return answer