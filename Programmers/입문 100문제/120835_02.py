def solution(emergency):
    # (인덱스, 응급도) 형태로 저장한 후, 응급도가 높은 순서대로 정렬
    sorted_emergency = sorted(enumerate(emergency), key=lambda x: -x[1])
    
    # 결과를 저장할 리스트
    answer = [0] * len(emergency)
    
    # 정렬된 순서대로 순위를 매김
    for rank, (index, _) in enumerate(sorted_emergency, start=1):
        answer[index] = rank
    
    return answer
