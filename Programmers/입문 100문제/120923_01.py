def solution(num, total):
    answer = []
    result = 0
    
    for i in range(num):
        result += i
    
    initialValue = (total-result)/num

    for i in range(num):
        answer.append(initialValue+i)
    
    return answer