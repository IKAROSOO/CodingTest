def solution(price, money, count):
    total_price = price * ((count+1)*count // 2)

    if money > total_price:
        return 0
    else:
        return total_price-money