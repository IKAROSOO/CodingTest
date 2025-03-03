def solution(s):
    s = list(map(str, s.split()))
    answerList = []
    answer = 0

    for element in s:
        if element != "Z":
            answerList.append(element)
        else:
            answerList.pop()
    
    for num in answerList:
        answer += int(num)
    
    return answer