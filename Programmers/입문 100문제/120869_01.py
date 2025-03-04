def solution(spell, dic):
    word_cnt = []

    for word in dic:
        cnt = 0

        for spelling in spell:
            if spelling in word:
                cnt += 1
            
        word_cnt.append(cnt)
    
    if max(word_cnt) == len(spell):
        return 1
    else:
        return 2