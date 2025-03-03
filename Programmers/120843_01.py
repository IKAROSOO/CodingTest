def solution(numbers, k):
    cnt = 2*(k-1)
    target = cnt%len(numbers)

    return numbers[target]