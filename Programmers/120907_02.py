def solution(quiz):
    answer = []

    for q in quiz:
        x, op , y, _, z = q.split()
        x, y, z = int(x), int(y), int(z)

        if op == "+":
            if x+y == z:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if x-y == z:
                answer.append("O")
            else:
                answer.append("X")
    
    return answer