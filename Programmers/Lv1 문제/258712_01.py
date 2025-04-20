def solution(friends, gifts):
    gift_point = dict.fromkeys(friends)
    # 각 friend가 서로에게 얼마나 선물을 주고받았는지 저장하는 dict
    gift_index = dict.fromkeys(friends, 0)
    # 각 friend의 최종적인 선물지수를 저장하는 dict
    monthly_gift = dict.fromkeys(friends, 0)
    # 최종적으로 월말에 받는 선물을 저장하는 dict

    for friend in friends:
        tmp = friends.copy()
        tmp.remove(friend)

        gift_point[friend] = dict.fromkeys(tmp, 0)

    for gift in gifts:
        giver, receiver = gift.split()

        gift_point[giver][receiver] += 1
        gift_point[receiver][giver] -= 1

        gift_index[giver] += 1
        gift_index[receiver] -= 1
    
    for friend in friends:
        tmp = friends.copy()
        tmp.remove(friend)

        for receiver in tmp:
            if gift_point[friend][receiver] > 0:
                monthly_gift[friend] += 1
            elif gift_point[friend][receiver] < 0:
                monthly_gift[receiver] += 1
            else:
                if gift_index[friend] > gift_index[receiver]:
                    monthly_gift[friend] += 1
                elif gift_index[friend] < gift_index[receiver]:
                    monthly_gift[receiver] += 1

    return max(monthly_gift.values())//2