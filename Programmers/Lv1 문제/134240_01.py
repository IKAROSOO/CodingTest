def solution(food):
    answer = ""

    for i in range(1, len(food)):
        answer += f"{i}"*(food[i]//2)
    
    answer = answer + "0" + answer[::-1]

    return answer