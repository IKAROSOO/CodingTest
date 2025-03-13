def solution(lottos, win_nums):
    cnt_0 = lottos.count(0)
    cnt = 0

    for i in range(6):
        skip = False
        for j in range(6):
            if lottos[i] == win_nums[j]:
                cnt += 1
                skip = True
                break
        if skip:
            continue
    
    best = 7 - (cnt+cnt_0)
    worst = 7 - cnt

    if cnt <= 1:
        worst = 6
    if cnt+cnt_0 <= 1:
        best = 6
    
    return [best, worst]