def solution(sizes):
    width_list = []
    height_list = []

    for s in sizes:
        s.sort()
    
    for s in sizes:
        width_list.append(s[0])
        height_list.append(s[1])

    return max(width_list) * max(height_list)