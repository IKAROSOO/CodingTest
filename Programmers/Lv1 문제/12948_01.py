def solution(num):
    '''주어진 전화번호의 뒷 4자리를 제외한 나머지를 *로 가려서 반환하는 함수를 작성하는 문제'''
    
    n = len(num)

    answer = "*"*(n-4) + num[-4:]

    return answer