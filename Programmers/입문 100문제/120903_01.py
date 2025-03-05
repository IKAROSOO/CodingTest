def solution(s1, s2):
    answer = 0

    for s1_char in s1:
        for s2_char in s2:
            if s1_char == s2_char:
                answer += 1

    return answer