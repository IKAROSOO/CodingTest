def solution(X, Y):
    x_cnt = [0] * 10
    y_cnt = [0] * 10
    answer = ""

    for x in X:
        x_cnt[int(x)] += 1
    for y in Y:
        y_cnt[int(y)] += 1

    for i in range(9, -1, -1):
        cnt = min(x_cnt[i], y_cnt[i])
        answer += str(i) * cnt
    
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer
