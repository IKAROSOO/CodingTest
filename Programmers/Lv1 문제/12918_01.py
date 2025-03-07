def solution(s):
    '''문자열의 길이가 4 또는 6이면서 숫자로만 구성되어 있는지 확인하여 참 또는 거짓을 반환'''

    if len(s) != 4:
        if len(s) != 6:
            return False

    for element in s:
        if not (ord(element) <= 57 and ord(element) >= 48):
            print(element)
            return False
    else:
        return True