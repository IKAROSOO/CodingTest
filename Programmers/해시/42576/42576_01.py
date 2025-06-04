def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    else:
        return participant[-1]

'''
해시로 푼 방법이 아님.
'''