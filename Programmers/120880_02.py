def solution(numlist, n):
    answer = []

    distance_list = []

    for num in numlist:
        distance = abs(num - n)
        distance_tuple = (distance, num)
        distance_list.append(distance_tuple)
    
    distance_list.sort(key=lambda x: (x[0], -x[1]))

    for distance_tuple in distance_list:
        num = distance_tuple[1]
        answer.append(num)

    return answer