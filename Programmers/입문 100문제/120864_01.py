def solution(my_string):
    answer = 0
    temp = 0

    for char in my_string:
        if char.isdigit():
            temp = temp * 10 + int(char)
        else:
            answer += temp
            temp = 0
    
    answer += temp

    return answer