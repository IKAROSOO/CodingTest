def solution(arr, divisor):
    answer = []
    arr.sort()

    for element in arr:
        if element%divisor == 0:
            answer.append(element)
    
    if answer:
        return answer
    else:
        return [-1]