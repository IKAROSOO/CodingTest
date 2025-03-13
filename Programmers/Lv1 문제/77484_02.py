def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    cnt_0 = lottos.count(0)
    cnt = 0

    for num in win_nums:
        if num in lottos:
            cnt += 1
    
    return rank[cnt_0+cnt], rank[cnt]