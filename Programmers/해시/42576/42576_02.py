def solution(participant, completion):
    hash = dict()

    for user in participant:
        hash[user] = hash.get(user, 0) + 1
    for user in completion:
        hash[user] -= 1
    
    for user, cnt in hash.items():
        if cnt > 0:
            return user