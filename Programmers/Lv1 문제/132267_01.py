def solution(a, b, n):
    '''빈 병 교환 규칙에 따라 최대 콜라 병 수 계산'''
    cnt = b*(n//a)
    empty = n%a

    n = cnt + empty

    while n >= a:
        tmp = 0
        tmp += b*(n//a)
        empty = n%a

        n = tmp + empty
        cnt += tmp

    return cnt