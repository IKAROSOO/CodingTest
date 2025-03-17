def solution(babbling):
    cnt = 0
    speakable = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        tmp = word
        prev_speak = ""

        while tmp:
            matched = False
            for speak in speakable:
                if tmp.startswith(speak) and speak != prev_speak:
                    tmp = tmp[len(speak):]
                    prev_speak = speak
                    matched = True
                    break
            if not matched:
                break
        if not tmp:
            cnt += 1
    return cnt

'''
제미나이가 풀어준 문제
'''