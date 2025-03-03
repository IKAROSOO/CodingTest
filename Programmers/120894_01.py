def solution(numbers):
    answer = ""
    temp = ""

    e_num = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "zero" : 0
    }

    for char in numbers:
        temp += char
        if temp in e_num:
            answer += str(e_num[temp])
            temp = ""
    
    return int(answer)