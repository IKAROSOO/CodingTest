def solution(n, lost, reserve):
    idx = 0
    cnt = 0

    lost_set = set(lost)
    reserve_set = set(reserve)

    And = lost_set & reserve_set

    for own in And:
        lost_set.remove(own)
        reserve_set.remove(own)
    
    lost_set = list(lost_set)
    reserve_set = list(reserve_set)
    
    while idx < len(lost_set):
        flag = False

        if reserve_set:
            for extra in reserve_set:
                if abs(lost_set[idx] - extra) == 1:
                    cnt += 1
                    flag = True
                    break
        
        else:
            break

        if flag:
            reserve_set.remove(extra)
        
        idx += 1

    return n - len(lost_set) + cnt

'''
Set()을 이용해서, 전처리 과정을 더욱 효율적으로 개선
'''