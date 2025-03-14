def solution(s):
    num_dict = {
        "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5,
        "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "zero" : 0
    }

    answer = ""
    s_cnt = ""

    for char in s:
        if char.isdigit():
            answer += char
        else:
            s_cnt += char
            if s_cnt in num_dict:
                answer += str(num_dict[s_cnt])
                s_cnt = ""

    return int(answer)