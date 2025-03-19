def solution(cards1, cards2, goal):
    cnt_1, cnt_2 = 0, 0

    for word in goal:
        if cnt_1 < len(cards1) and word == cards1[cnt_1]:
            cnt_1 += 1
        elif cnt_2 < len(cards2) and word == cards2[cnt_2]:
            cnt_2 += 1
        else:
            return "No"
    
    return "Yes"