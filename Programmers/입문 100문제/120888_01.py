def solution(my_string):
    answer = ""

    for spelling in my_string:
        if spelling not in answer:
            answer += spelling
    
    return answer