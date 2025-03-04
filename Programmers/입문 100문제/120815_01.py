def solution(n):
    answer = 1

    while(True):
        pizza = answer * 6
        if pizza%n == 0:
            break
        answer += 1

    return answer