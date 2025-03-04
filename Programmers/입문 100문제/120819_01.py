def solution(money):
    answer = []

    iA = money//5500
    change = money%5500

    answer.append(iA)
    answer.append(change)

    return answer