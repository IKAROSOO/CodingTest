def solution(progresses, speeds):
    n = len(progresses)
    answer = list()
    time = [0 for _ in range(n)]

    for i in range(n):
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            time[i] += 1
    
    max_time = time[0]
    cnt = 1

    for i in range(1, n):
        if time[i] <= max_time:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_time = time[i]
    
    answer.append(cnt)

    return answer