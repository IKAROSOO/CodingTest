def solution(s, skip, index):
    answer = ""

    skip_list = list(skip)

    for char in s:
        tmp = char
        cnt = 0

        while cnt < index:
            tmp = chr(ord(tmp) + 1)

            if ord(tmp) > ord("z"):
                tmp = "a"

            if tmp in skip_list:
                continue
            else:
                cnt += 1
        answer += tmp
    
    return answer