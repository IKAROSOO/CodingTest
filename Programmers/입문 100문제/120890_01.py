def solution(array, n):
    distance_ary = []

    for num in array:
        distance_ary.append(abs(num - n))
    
    min_distance = min(distance_ary)

    if n+min_distance in array and n-min_distance in array:
        return n-min_distance
    else:
        return array[distance_ary.index(min(distance_ary))]