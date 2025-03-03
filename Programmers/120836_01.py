def solution(n):
    answer = 0
    testNum = 1

    while testNum <= n:
        if n % testNum == 0:
            answer += 1
            print(testNum)
        
        testNum += 1

    return answer