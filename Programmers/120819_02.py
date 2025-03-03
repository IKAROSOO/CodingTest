def solution(money):
    answer = []

    iA = money//5500
    change = money%5500

    answer.extend([iA, change])

    return answer