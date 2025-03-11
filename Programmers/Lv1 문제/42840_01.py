def solution(answers):
    '''수포자 3명의 찍기 패턴과 정답 배열(answers)이 주어졌을 때,
    각 수포자의 정답 수를 계산하고 가장 많은 정답을 맞힌 수포자를 찾는 문제'''

    math1, math1_cnt = [1, 2, 3, 4, 5] * len(answers), 0
    math2, math2_cnt = [2, 1, 2, 3, 2, 4, 2, 5] * len(answers), 0
    math3, math3_cnt = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * len(answers), 0

    for num in range(len(answers)):
        if math1[num] == answers[num]:
            math1_cnt += 1
        if math2[num] == answers[num]:
            math2_cnt += 1
        if math3[num] == answers[num]:
            math3_cnt += 1
    
    a = [math1_cnt, math2_cnt, math3_cnt]
    max_cnt = max(a)

    return list(i+1 for i in range(3) if a[i] == max_cnt)