def solution(d, budget):
    '''정해진 예산 안에서 최대한 많은 부서에 필요한 물품을 지원하는 문제'''

    cnt = 0
    d.sort()

    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            break
        cnt += 1
    
    return cnt