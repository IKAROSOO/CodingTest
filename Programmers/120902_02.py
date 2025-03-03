def solution(my_string):
    char_list = my_string.split()
    res = int(char_list[0])

    for i in range(1, len(char_list), 2):

        if char_list[i] == "+":
            res += int(char_list[i+1])
        else:
            res -= int(char_list[i+1])
    
    return res