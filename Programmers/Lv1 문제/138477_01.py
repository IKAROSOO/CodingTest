def solution(k, score):
    answer = []
    honor_list = []
    day = 0

    for i in range(len(score)):
        if day < k:
            honor_list.append(score[i])
            answer.append(min(honor_list))
        else:
            if score[i] > min(honor_list):
                honor_list.remove(min(honor_list))
                honor_list.append(score[i])
                answer.append(min(honor_list))
            else:
                answer.append(min(honor_list))
        day += 1
    
    return answer