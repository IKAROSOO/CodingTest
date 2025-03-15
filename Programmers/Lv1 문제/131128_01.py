def solution(X, Y):
    answer = ""

    x_list = []
    y_list = []
    intersection = []

    for num in X:
        x_list.append(num)
    for num in Y:
        y_list.append(num)

    x_list.sort(); y_list.sort()

    for num in x_list:
        if num in y_list:
            intersection.append(num)
            y_list.remove(num)
    
    if not intersection:
        return "-1"
    
    while intersection:
        answer += max(intersection)
        intersection.remove(max(intersection))
    
    if int(answer) == 0:
        return "0"
    else:
        return answer

'''
로직은 옳지만, 시간복잡도가 너무 크다.
시간복잡도 : O(n^2)
'''