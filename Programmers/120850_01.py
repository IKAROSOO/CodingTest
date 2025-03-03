def solution(my_string):
    answer = []
    numbers = ['0', '1', '2', '3', '4',
            '5', '6', '7', '8', '9']

    for char in my_string:
        if char in numbers:
            answer.append(int(char))
    
    answer.sort()

    return answer