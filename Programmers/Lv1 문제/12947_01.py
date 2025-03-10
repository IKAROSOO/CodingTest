def solution(x):
    harshad_num = 0

    for i in range(len(str(x))):
        harshad_num += int(str(x)[i])
    
    if not x%harshad_num:
        return True
    else:
        return False