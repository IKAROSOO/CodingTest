def solution(s):
    cnt = 0

    sav1 = 0
    sav2 = 0

    for i in s:
        if sav1 == sav2:
            cnt += 1
            a = i
        
        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    
    return cnt

'''
솔직히 이해 잘 안됨
'''