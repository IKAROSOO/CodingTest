def solution(id_list, report, k):
    answer = []

    id_dict = {}
    report_dict = {}
    report = list(set(report))


    for user in id_list:
        id_dict[user] = 0
        report_dict[user] = 0

    for i in range(len(report)):
        user, reported = report[i].split(" ")
        
        report_dict[reported] += 1

    for i in range(len(report)):
        user, reported = report[i].split(" ")

        if report_dict[reported] >= k:
            id_dict[user] += 1
    
    for user in id_list:
        answer.append(id_dict[user])
    
    return answer