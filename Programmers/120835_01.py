def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        answer.append(0)

    priority = 1
    
    while True:
        flag = False

        maxNum = max(emergency)
        maxIndex = 0

        for num in range(len(emergency)):
            if emergency[num] == maxNum:
                maxIndex = num
        
        answer[maxIndex] = priority
        
        emergency[maxIndex] = 0
        priority += 1

        for i in emergency:
            if i != 0:
                flag = True
                break
        
        if not flag:
            break
    
    return answer
