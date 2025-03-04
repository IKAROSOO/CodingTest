def solution(score):
    answer = []
    score_list = []
    
    # 학생들의 (인덱스, 평균 점수) 리스트 생성
    for index in range(len(score)):
        score_list.append((index + 1, sum(score[index])))
    
    # 평균 점수 기준으로 내림차순 정렬
    sorted_score_list = sorted(score_list, key=lambda x: -x[1])
    
    # 순위 계산
    rank = 1
    ranked_score_list = []
    
    i = 0
    while i < len(sorted_score_list):
        current_score = sorted_score_list[i][1]
        count = 1
        
        # 동점자 수 계산
        while i + count < len(sorted_score_list) and sorted_score_list[i + count][1] == current_score:
            count += 1
        
        # 동점자에게 동일한 순위 부여
        for j in range(count):
            ranked_score_list.append((sorted_score_list[i + j][0], rank))
        
        # 다음 순위 계산
        rank += count
        i += count
    
    # 학생 인덱스 순으로 정렬하여 최종 순위 반환
    ranked_score_list.sort(key=lambda x: x[0])
    
    for _, r in ranked_score_list:
        answer.append(r)
    
    return answer