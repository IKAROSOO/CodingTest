def solution(n):
    n_2 = str(bin(n)[2:])
    num = n+1
    cnt_1 = 0
    
    for a in n_2:
        if a == "1":
            cnt_1 += 1
    
    while True:
        num_2 = bin(num)[2:]
        cnt = 0
        
        for number in num_2:
            if number == "1":
                cnt += 1
        
        if cnt == cnt_1:
            return num
        
        num += 1
        
'''
2025_06_05_14:19
'''