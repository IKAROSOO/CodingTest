def solution(lines):
    answer = 0
    
    maxNum = 0
    minNum = 0

    for i in range(len(lines)):
        if max(lines[i]) > maxNum:
            maxNum = max(lines[i])
        if minNum > min(lines[i]):
            minNum = min(lines[i])

    horizontalLine = [0 for i in range(minNum, maxNum)]

    for i in range(len(lines)):
        for j in range(lines[i][0] - minNum, lines[i][1] - minNum):
            horizontalLine[j] += 1

    for i in range(len(horizontalLine)):
        if horizontalLine[i] >= 2:
            answer += 1

    return answer