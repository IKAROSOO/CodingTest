def solution(n):
    '''n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return'''

    tenary = ""
    answer = 0
    
    while n != 0:
        tenary += (str(n%3))
        
        n //= 3
    
    for i in range(len(tenary)):
        answer += int(tenary[i]) * (3**(len(tenary) - i - 1))
    
    return answer