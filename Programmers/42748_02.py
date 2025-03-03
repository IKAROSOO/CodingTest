def solution(array, commands):
    answer = []

    for command in commands:
        i, j, k = command
        cutted = []
        
        cutted = array[i-1:j]
        cutted.sort()

        answer.append(cutted[k-1])

    return answer