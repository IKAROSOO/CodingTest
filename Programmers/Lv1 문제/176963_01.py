def solution(name, yearning, photo):
    score_dict = {}
    score_list = []

    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    
    for i in range(len(photo)):
        score = 0

        for j in range(len(photo[i])):
            if photo[i][j] in score_dict:
                score += score_dict[photo[i][j]]
        score_list.append(score)
    
    return score_list