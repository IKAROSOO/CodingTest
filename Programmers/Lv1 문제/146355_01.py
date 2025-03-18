def solution(t, p):
    cnt = 0

    for i in range(0, len(t)-len(p)+1):
        tmp = int(t[i:i+len(p)])

        if int(p) >= tmp:
            cnt += 1

    return cnt