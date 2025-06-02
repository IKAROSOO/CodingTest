def solution(arr):
    answer = list()
    before = -1

    for num in arr:
        if num == before:
            continue
        answer.append(num)
        before = num
    
    return answer