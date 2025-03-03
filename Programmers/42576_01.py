def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]

'''
해당 문제는 O(n^2)으로 풀면 안된다.
'''