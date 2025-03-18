def solution(s):
    cnt = 0
    index = 0
    
    standard = s[index]
    standard_cnt = 0
    nonStandard_cnt = 0

    while True:
        if index >= len(s):
            cnt += 1
            break

        if s[index] == standard:
            standard_cnt += 1
        else:
            nonStandard_cnt += 1

        if standard_cnt == nonStandard_cnt:
            try:
                s = s[:0] + s[standard_cnt+nonStandard_cnt:]
                index, standard_cnt, nonStandard_cnt = 0, 0, 0
                standard = s[index]
                cnt += 1
                continue
            except:
                cnt += 1
                break

        index += 1
    
    return cnt

'''
시간복잡도 : O(n^2)
'''