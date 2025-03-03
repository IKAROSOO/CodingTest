def solution(score):
    score_list = sorted([sum(i) for i in score], reverse= True)
    # -> 리스트의 각 원소를 합한 후 내림차순으로 정렬

    ranked_list = [score_list.index(sum(i))+1 for i in score]
    # -> 원소의 합과 같은 값인 원소의 index를 찾아낸다.
    # -> 해당 index+1을 하여 등수를 매긴다.
    # -> 동점의 경우 index는 작은값을 우선으로 매긴다.