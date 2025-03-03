def solution(array, commands):
    answer = []

    n = len(commands)

    for i in range(n):
        cnt = commands[i][0]
        cutted = []

        while(cnt <= commands[i][1]):
            cutted.append(array[cnt-1])
            cnt += 1

        cutted.sort()
        answer.append(cutted[commands[i][2]-1])

    return answer