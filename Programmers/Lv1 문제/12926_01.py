def solution(s, n):
    '''주어진 문자열을 특정 거리만큼 밀어서 암호화하는 시저 암호 함수를 구현하는 문제'''

    answer = ""

    for char in s:
        if ord(char) >= 65 and ord(char) <= 90:
            # 문자열의 각 문자가 대문자인 경우
            num = ord(char) + n
            if num > 90:
                num -= 26
            
            answer += chr(num)
        elif ord(char) >= 97 and ord(char) <= 122:
            # 문자열의 각 문자가 소문자인 경우
            num = ord(char) + n
            if num > 122:
                num -= 26
            
            answer += chr(num)
        else:
            answer += char
    
    return answer