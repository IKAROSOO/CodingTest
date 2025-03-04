def solution(common):
    Asequence = []
    Gsequence = []

    for i in range(1, len(common)):
        Asequence.append(common[i] - common[i-1])
        Gsequence.append(common[i] - common[i-1])
    
    if Asequence[0] == Asequence[1]:
        return common[-1] + Asequence[0]
    else:
        return common[-1] * (common[1]/common[0])