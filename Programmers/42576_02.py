def solution(participant, completion):
    names = {}

    for name in participant:
        if name not in names:
            names[name] = 0
        names[name] += 1
    
    for name in participant:
        names[name] -= 1
    
    for key, value in names.items():
        if value == 1:
            return key

'''
O(n)으로 해결한 문제

해시맵을 이용해서 문제를 해결한 것
'''