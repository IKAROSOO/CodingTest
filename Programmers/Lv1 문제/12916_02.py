def solution(s):
    '''주어진 문자열에서 'p'와 'y'의 개수를 대소문자 구분 없이 세어 비교하고,
    두 개수가 같으면 참, 다르면 거짓을 반환'''

    cnt = 0

    for element in s:
        if element == "p" or element == "P":
            cnt += 1
        elif element == "y" or element == "Y":
            cnt -= 1
    else:
        if not cnt:
            return True
        else:
            return False