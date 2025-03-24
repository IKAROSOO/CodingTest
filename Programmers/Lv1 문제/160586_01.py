def solution(keymap, targets):
    answer = []
    
    for target in targets:
        cnt = 0
        for i in range(len(target)):
            min_index = float('inf')
            for key in keymap:
                if target[i] in key:
                    tmp = key.index(target[i])
                    min_index = min(min_index, tmp)
            if min_index == float('inf'):
                cnt = -1
                break
            else:
                cnt += min_index + 1
        answer.append(cnt)
    
    return answer