def solution(num_list, n):
    answer = []
    cnt = 0
    insert_list = []


    while cnt < len(num_list):
        insert_list.append(num_list[cnt])
        cnt += 1

        if len(insert_list) == n:
            answer.append(insert_list)
            insert_list = []
    
    return answer