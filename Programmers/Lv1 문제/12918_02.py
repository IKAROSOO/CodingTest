def solution(s):
    '''문자열의 길이가 4 또는 6이면서 숫자로만 구성되어 있는지 확인하여 참 또는 거짓을 반환'''

    try:
        int(s)
    except:
        return False
    
    return len(s)== 4 or len(s) == 6