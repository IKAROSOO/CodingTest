def solution(numbers, direction):
    if direction == "right":
        tmp = numbers[-1]

        for i in range(len(numbers) - 1, 0, -1):
            numbers[i] = numbers[i-1]
            print(numbers)
        
        numbers[0] = tmp
    else:
        tmp = numbers[0]
        
        for i in range(len(numbers)-1):
            numbers[i] = numbers[i+1]
            print(numbers)
        
        numbers[-1] = tmp

    return numbers