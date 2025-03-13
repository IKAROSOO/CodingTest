def solution(absolutes, signs):
    '''절댓값 배열과 부호 배열을 사용하여 실제 정수들의 합을 구하는 함수를 완성하는 문제'''

    answer = 0

    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num
    
    return answer