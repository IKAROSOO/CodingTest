def solution(n):
    '''정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수'''

    answer = 0

    for i in range(1, int(n*0.5)+1):
        if n % i == 0:
            answer += i
    
    return answer+n