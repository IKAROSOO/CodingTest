def solution(s):
    unique_char = []

    for char in s:
        if s.count(char) == 1:
            unique_char.append(char)
    
    answer = "".join(sorted(unique_char))

    return answer