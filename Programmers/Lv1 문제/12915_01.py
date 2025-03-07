def solution(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    answer = []
    alphabet_list = []

    for char in strings:
        alphabet_list.append((char[n], char))
    
    alphabet_list.sort()

    for char in alphabet_list:
        answer.append(char[1])
    
    return answer