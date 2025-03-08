def solution(n):
    '''주어진 숫자(n)만큼 "수박" 패턴을 반복하는 문자열을 만드는 함수를 작성'''

    answer = ""

    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"
    
    return answer