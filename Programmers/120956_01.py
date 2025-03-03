def solution(babbling):
    answer = 0
    canSpeak = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        for speak in canSpeak:
            if speak*2 in word:
                break
            word = word.replace(speak, " ", 1)  # 1 : 최대 1번만 replace 가능
        if word.strip() == "":
            answer += 1

    return answer

# 다시 풀어봐야 함