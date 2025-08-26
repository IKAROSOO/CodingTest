def solution(n, lost, reserve):
    idx = 0
    cnt = 0
    own_list = list()

    lost.sort()
    reserve.sort()

    for losted in lost:
        for extra in reserve:
            if losted == extra:
                own_list.append(losted)
    
    for own in own_list:
        lost.remove(own)
        reserve.remove(own)

    while idx < len(lost):
        flag = False
        
        if reserve:
            for extra in reserve:
                if abs(lost[idx] - extra) <= 1:
                    cnt += 1
                    flag = True
                    tmp = extra
                    break
        else:
            break
                    
        if flag:
            reserve.remove(tmp)
        
        idx += 1
    
    return n - len(lost) + cnt