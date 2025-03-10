def solution(x, n):
    '''정수 x 부터 시작해서 x 씩 증가하는 숫자를 n개
    가지는 리스트를 반환하는 함수를 작성하는 문제입니다.'''

    if x:
        return list(i for i in range(x, x*(n+1), x))
    else:
        return [0]*n