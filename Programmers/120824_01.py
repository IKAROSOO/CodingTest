def solution(num_list):
    answer = []

    evenCnt = 0
    oddCnt = 0

    for number in num_list:
        if number % 2 == 0:
            evenCnt += 1
        else:
            oddCnt += 1
    
    answer.append(evenCnt)    
    answer.append(oddCnt)

    return answer