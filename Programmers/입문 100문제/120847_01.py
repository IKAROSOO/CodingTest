def solution(numbers):
    firstNum = max(numbers)
    numbers.remove(firstNum)

    secondNum = max(numbers)

    return firstNum*secondNum