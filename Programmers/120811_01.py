def solution(array):
    array.sort()

    n = len(array)

    answer = n//2

    return array[answer]