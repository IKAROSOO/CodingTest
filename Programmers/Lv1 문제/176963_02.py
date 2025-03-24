def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    scores = []

    for pt in photo:
        score = 0
        for p in pt:
            if p in score_dict:
                score += score_dict[p]
        
        scores.append(score)
    
    return score