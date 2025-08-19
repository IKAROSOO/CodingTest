def solution(msg):
    # 아스키값 기준으로 A는 65
    answer = list()
    new_dict = dict()
    tmp = ""

    for i in range(1, 27):
        new_dict[chr(i+64)] = i

    for i in range(len(msg)):
        if msg[i] in 


    print(new_dict)

solution("KAKAO")