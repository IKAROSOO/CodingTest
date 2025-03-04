def solution(s):
    value_ary = []
    alphabet_dict = {}

    for char in s:
        if char in alphabet_dict:
            alphabet_dict[char] += 1
        else:
            alphabet_dict[char] = 1
    
    for key, value in alphabet_dict.items():
        if value == 1:
            value_ary.append(key)
    
    answer = "".join(sorted(value_ary))

    return answer