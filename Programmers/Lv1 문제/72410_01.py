def solution(new_id):
    step_1 = new_id.lower()
    # 1단계 clear

    step_2 = ""
    del_list = ["!", "@", "#", "*"]
    serve_list = ["-", "_", "."]
    for char in step_1:
        if char in serve_list or char.isalpha() or char.isdigit():
            step_2 += char
        else:
            continue
    # 2단계 clear

    step_3 = ""
    cnt = 0
    for char in step_2:
        if char == ".":
            cnt += 1
            if cnt < 2:
                step_3 += char
        else:
            step_3 += char
            cnt = 0
    # 3단계 clear

    step_4 = step_3
    tmp = ""
    if step_3 and step_3[0] == ".":
        tmp = step_3[1:]
        step_4 = tmp

        if tmp and tmp[-1] == ".":
            step_4 = tmp[:-1]
    elif step_3 and step_3[-1] == ".":
        step_4 = step_3[:-1]
    # 4단계 clear

    step_5 = step_4
    if not step_4:
        step_5 += "a"
    # 5단계 clear
    
    step_6 = step_5
    if len(step_5) >= 16:
        step_6 = step_5[:15]

        if step_6[-1] == ".":
            step_6 = step_6[:-1]
    # 6단계 clear

    step_7 = step_6
    if len(step_7) <= 2:
        while len(step_7) != 3:
            step_7 += step_7[-1]
    
    return step_7