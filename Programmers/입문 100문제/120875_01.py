def solution(dots):
    answer = 0

    line1_1 = dots.pop(0)
    
    for i in range(3):
        line1_2 = dots[i]
        line2_1 = dots[(i+1)%3]
        line2_2 = dots[(i+2)%3]

        if (checkDegree(line1_1, line1_2) ==
            checkDegree(line2_1, line2_2)):
            answer = 1

    return answer

def checkDegree(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2

    return (y2-y1)/(x2-x1)