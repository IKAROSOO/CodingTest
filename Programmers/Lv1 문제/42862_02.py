def solution(n, lost, reverse):
    '''도난당한 학생과 여벌 옷을 가져온 학생 목록을 활용하여
    최대한 많은 학생이 체육복을 입을 수 있도록 배분'''

    reverse_set = set(reverse) - set(lost)
    # reverse에 속하면서 lost에도 속하는 element 제거
    lost_set = set(lost) - set(reverse)
    # 위에서 제거한 element를 반영

    for r in sorted(reverse_set):
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)

    return n - len(lost_set)