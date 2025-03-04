def solution(quiz):
    answer = []

    for element in quiz:
        cal = eval(element.partition("= ")[0])
        res = int(element.partition("= ")[2])

        if cal == res:
            answer.append("O")
        else:
            answer.append("X")
    
    return answer