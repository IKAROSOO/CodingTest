def solution(dots):
    answer = 0

    line1_1 = dots[0]  # 첫 번째 점 선택

    for i in range(1, 4):  # i는 1부터 3까지
        line1_2 = dots[i]  # 점을 순차적으로 선택
        line2_1 = dots[(i+1)%4]  # 나머지 점들
        line2_2 = dots[(i+2)%4]

        # 기울기 비교
        if checkDegree(line1_1, line1_2) == checkDegree(line2_1, line2_2):
            answer += 1

    return answer

def checkDegree(dot1, dot2):
    x1, y1 = dot1
    x2, y2 = dot2

    # 기울기 계산
    return (y2 - y1) / (x2 - x1)

# 예시 실행
print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))  # 1이 나와야 함
