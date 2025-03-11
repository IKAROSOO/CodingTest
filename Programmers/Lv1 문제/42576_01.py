def solution(participant, completion):
    '''마라톤 참가자 명단(participant)과 완주자 명단(completion)이 주어졌을 때,
    완주하지 못한 단 한 명의 참가자를 찾아내는 함수를 작성'''
    
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    else:
        return participant[-1]