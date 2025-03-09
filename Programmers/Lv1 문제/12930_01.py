def solution(s):
    '''주어진 문자열에서 각 단어의 짝수 번째 문자는 대문자로,
    홀수 번째 문자는 소문자로 변환하여 반환하는 함수를 작성'''

    cnt = 1
    answer = ""

    for char in s:
        if char == " ":
            cnt = 1
            answer += char
            continue
        
        if cnt % 2 != 0:
            answer += char.upper()
        else:
            answer += char.lower()
        
        cnt += 1
    
    print(answer)

    return answer

solution("try hello world")