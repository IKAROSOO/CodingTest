def solution(clothes):
    cnt = 1
    cloth_dict = dict()
    
    for i in range(len(clothes)):
        cloth_dict[clothes[i][1]] = cloth_dict.get(clothes[i][1], 0) + 1
    
    if len(cloth_dict) > 1:
        for _, amount in cloth_dict.items():
            cnt *= (amount+1)
    else:
        for amount in cloth_dict.values():
            cnt += amount
    
    cnt -= 1
    
    return cnt