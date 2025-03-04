def solution(dots):
    x_min = min(dots[0][0], dots[1][0], dots[2][0], dots[3][0])
    x_max = max(dots[0][0], dots[1][0], dots[2][0], dots[3][0])

    y_min = min(dots[0][1], dots[1][1], dots[2][1], dots[3][1])
    y_max = max(dots[0][1], dots[1][1], dots[2][1], dots[3][1])

    len_x = x_max - x_min
    len_y = y_max - y_min

    print(len_x, len_y)

    return int(len_x*len_y)