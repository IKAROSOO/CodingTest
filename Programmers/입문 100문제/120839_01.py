def solution(rsp):
    answer = ""

    for game in rsp:
        if game == str(2):
            answer += str(0)
        elif game == str(0):
            answer += str(5)
        else:
            answer += str(2)

    return answer