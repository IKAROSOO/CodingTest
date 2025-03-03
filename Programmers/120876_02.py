def solution(lines):
    answer = 0

    minNum = min(lines[0])
    maxNum = max(lines[0])

    for i in range(1, len(lines)):
        minNum = min(minNum, min(lines[i]))
        maxNum = max(maxNum, max(lines[i]))

    horizontalLine = [0] * (maxNum - minNum)

    for i in range(len(lines)):
        for j in range(lines[i][0] - minNum, lines[i][1] - minNum):
            horizontalLine[j] += 1

    for i in range(len(horizontalLine)):
        if horizontalLine[i] >= 2:
            answer += 1

    return answer

# 제미나이가 알려준 개선된 코드