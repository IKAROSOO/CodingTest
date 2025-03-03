def solution(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    answer = ""

    for spelling in my_string:
        if spelling not in vowels:
            print(spelling)
            answer += spelling
    
    return answer