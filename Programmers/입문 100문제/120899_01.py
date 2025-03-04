def solution(array):
    answer = []

    answer.append(max(array))
    answer.append(array.index(max(array)))

    return answer

# -> return [max(array), array.index(max(array))]