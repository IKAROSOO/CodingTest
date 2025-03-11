def solution(dartResult):
    '''다트 게임에서 얻은 점수와 영역(S, D, T),
    옵션(*, #)을 조합하여 총 점수를 계산하는 함수를 작성'''

    score_list = []
    prize_list = []
    cnt = 0
    index_temp = 0

    for i in range(len(dartResult)):
        if dartResult[i] == "S" or dartResult[i] == "D" or dartResult[i] == "T":
            if dartResult[i] == "S":
                score_list.append(int(dartResult[index_temp : i]))
                index_temp = i+1
                cnt +=1
            elif dartResult[i] == "D":
                score_list.append(int(dartResult[index_temp : i])**2)
                index_temp = i+1
                cnt +=1
            elif dartResult[i] == "T":
                score_list.append(int(dartResult[index_temp : i])**3)
                index_temp = i+1
                cnt +=1

        elif dartResult[i] == "*" or dartResult[i] == "#":
            index_temp += 1
    
    for prize, cnt in prize_list:
        if prize == "*":
            if cnt - 2 < 0:
                score_list[cnt-1] *= 2
            else:
                score_list[cnt-1] *= 2
                score_list[cnt-2] *= 2
        elif prize == "#":
            score_list[cnt-1] *= -1
    
    return sum(score_list)