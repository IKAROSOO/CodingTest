def solution(numbers, hand):
    res = []

    left_loc = "*"
    right_loc = "#"

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            res.append("L")
            left_loc = f"{num}"
            continue
        elif num == 3 or num == 6 or num == 9:
            res.append("R")
            right_loc = f"{num}"
            continue
        right_dis, left_dis = distance(right_loc, num), distance(left_loc, num)
        print(right_dis, left_dis)
        print(type(right_dis))
        
        if right_dis == left_dis:
            if hand == "right":
                res.append("R")
                right_loc = f"{num}"
                continue
            else:
                res.append("L")
                left_loc = f"{num}"
                continue
        else:
            if min(right_dis, left_dis) == right_dis:
                res.append("R")
                right_loc = f"{num}"
                continue
            else:
                res.append("L")
                left_loc = f"{num}"
                continue

    return "".join(res)

def distance(hand, target):
    if hand == "1" or hand == "3":
        if target == 2:
            return 1
        elif target == 5:
            return 2
        elif target == 8:
            return 3
        elif target == 0:
            return 4
    elif hand == "4" or hand == "6":
        if target == 2:
            return 2
        elif target == 5:
            return 1
        elif target == 8:
            return 2
        elif target == 0:
            return 3
    elif hand == "7" or hand == "9":
        if target == 2:
            return 3
        elif target == 5:
            return 2
        elif target == 8:
            return 1
        elif target == 0:
            return 2
    elif hand == "*" or hand == "#":
        if target == 2:
            return 4
        elif target == 5:
            return 3
        elif target == 8:
            return 2
        elif target == 0:
            return 1
    elif hand == "2":
        if target == 2:
            return 0
        elif target == 5:
            return 1
        elif target == 8:
            return 2
        elif target == 0:
            return 3
    elif hand == "5":
        if target == 2:
            return 1
        elif target == 5:
            return 0
        elif target == 8:
            return 1
        elif target == 0:
            return 2
    elif hand == "8":
        if target == 2:
            return 2
        elif target == 5:
            return 1
        elif target == 8:
            return 0
        elif target == 0:
            return 1
    elif hand == "0":
        if target == 2:
            return 3
        elif target == 5:
            return 2
        elif target == 8:
            return 1
        elif target == 0:
            return 0

solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")