def solution(d, budget):
    answer = 0

    d.sort()

    for cost in d:
        budget -= cost
        if(budget >= 0):
            answer += 1

    return answer