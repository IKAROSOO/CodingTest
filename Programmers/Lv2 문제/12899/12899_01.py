def solution(n):
    num_list = list()
    
    while n // 3 >= 1:
        a = n // 3
        b = n % 3
        
        if b == 0:
            num_list.append(4)
            a -= 1
        else:
            num_list.append(b)
        
        n = a
    
    if n%3:
        num_list.append(n%3)
    
    num_list = num_list[::-1]
    num = "".join(map(str, num_list))
    int(num)
    
    return num