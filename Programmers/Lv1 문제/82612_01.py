def solution(price, money, count):
    cnt = 0

    while cnt != count:
        cnt += 1
        money -= price*cnt

    if money > 0:
        return 0
    else:
        return abs(money)