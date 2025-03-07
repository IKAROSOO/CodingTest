def solution(s):
    '''주어진 문자열에서 'p'와 'y'의 개수를 대소문자 구분 없이 세어 비교하고,
    두 개수가 같으면 참, 다르면 거짓을 반환'''

    s = s.lower()
    # lower() : 문자열의 모든 문자를 소문자로 바꾸는 함수

    return s.count("p") == s.count("y")