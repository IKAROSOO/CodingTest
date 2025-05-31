def solution(id_list, report, k):
    id_dict = dict()            # 각 유저의 신고 성공을 저장하는 딕셔너리
    report_dict = dict()        # 각 유저가 신고당한 횟수를 저장한는 딕셔너리
    report = list(set(report))  # 중복으로 신고한 것을 제외
    answer = []
    
    for i in range(len(report)):
        user, reported = report[i].split(" ")   # 신고자와 피신고자 구분분

        if reported not in report_dict:         # 딕셔너리에 해당 유저가 없는 경우우
            report_dict[reported] = 1
        else:
            report_dict[reported] += 1
    
    for reporting in report:
        user, reported = reporting.split(" ")

        if report_dict[reported] >= k:          # 피신고자의 누적 경고수가 기준을 넘을 경우
            if user not in id_dict:
                id_dict[user] = 1
                continue
            id_dict[user] += 1
    
    for user in id_list:
        if user not in id_dict:
            answer.append(0)
            continue
        answer.append(id_dict[user])
    
    return answer