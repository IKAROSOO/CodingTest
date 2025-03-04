def solution(order):
    cnt = 0

    for i in range(len(str(order))):
        str(order)[i]
        if str(order)[i] == "3" or str(order)[i] == "6" or str(order)[i] == "9":
            cnt +=1
    
    return cnt