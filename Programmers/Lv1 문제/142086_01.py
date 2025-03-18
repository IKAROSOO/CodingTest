def solution(s):
    answer = []
    alphabet_dict = {}

    for i, char in enumerate(s):
        if char not in alphabet_dict:
            alphabet_dict[char] = [char, i]
            answer.append(-1)
        else:
            answer.append(i - alphabet_dict[char][1])
            alphabet_dict[char][1] = i
        
    return answer