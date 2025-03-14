def solution(sizes):
    max_width = max(max(x) for x in sizes)
    max_height = max(min(x) for x in sizes)

    return max_height * max_width