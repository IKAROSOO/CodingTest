def solution(array):
    answer = 0

    for num in array:
        for i in range(len(str(num))):
            num_str = str(num)
            if str(num_str[i]) == "7":
                answer += 1
    
    return answer