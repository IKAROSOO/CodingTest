def solution(babbling):
    cnt = 0

    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j*2 not in i:
                i = i.replace(j, " ")
        if len(i.strip()) == 0:
            cnt += 1
    
    return cnt