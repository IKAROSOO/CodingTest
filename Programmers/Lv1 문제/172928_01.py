def solution(park, routes):
    startPoint = []

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S":
                startPoint = [i, j]

    for route in routes:
        direction, distance = route.split(" ")
        distance = int(distance)  # distance를 정수로 변환
        current_point = startPoint[:]  # 현재 위치 복사

        valid = True
        for _ in range(distance):
            if direction == "E":
                next_point = [current_point[0], current_point[1] + 1]
            elif direction == "W":
                next_point = [current_point[0], current_point[1] - 1]
            elif direction == "S":
                next_point = [current_point[0] + 1, current_point[1]]
            elif direction == "N":
                next_point = [current_point[0] - 1, current_point[1]]

            if (next_point[0] < 0 or next_point[0] >= len(park) or
                    next_point[1] < 0 or next_point[1] >= len(park[0]) or
                    park[next_point[0]][next_point[1]] == "X"):
                valid = False
                break
            current_point = next_point

        if valid:
            startPoint = current_point

    return startPoint