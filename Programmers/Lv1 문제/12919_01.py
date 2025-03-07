def solution(seoul):
    '''주어진 문자열 배열에서 "Kim"의 위치를 찾아 "김서방은 x에 있다" 형태의 문자열을 반환'''

    loc = seoul.index("Kim")

    return f"김서방은 {loc}에 있다"