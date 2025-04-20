def optimized_solution(friends, gifts):
    gift_point = {giver: {receiver: 0 for receiver in friends if receiver != giver} for giver in friends}
    gift_index = {friend: 0 for friend in friends}
    monthly_gift = {friend: 0 for friend in friends}

    for gift in gifts:
        giver, receiver = gift.split()
        gift_point[giver][receiver] += 1
        gift_point[receiver][giver] -= 1
        gift_index[giver] += 1
        gift_index[receiver] -= 1

    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            friend1 = friends[i]
            friend2 = friends[j]

            if gift_point[friend1].get(friend2, 0) > 0:
                monthly_gift[friend1] += 1
            elif gift_point[friend1].get(friend2, 0) < 0:
                monthly_gift[friend2] += 1
            else:
                if gift_index[friend1] > gift_index[friend2]:
                    monthly_gift[friend1] += 1
                elif gift_index[friend1] < gift_index[friend2]:
                    monthly_gift[friend2] += 1

    return max(monthly_gift.values())