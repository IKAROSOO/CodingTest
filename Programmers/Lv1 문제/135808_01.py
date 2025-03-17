def solution(k, m, score):
    score = sorted(score, reverse=True)
    boxes = [0] * len(score) // m
    tmp = 0
    answer = 0
    
    for box in boxes:
        box = list(score[tmp:tmp+m])
        tmp += m

        answer += min(box)*len((box))
    
    return