def solution(my_string):
    answer = 0

    for num in my_string:
        try:
            answer += int(num)
        except:
            pass
    
    return answer