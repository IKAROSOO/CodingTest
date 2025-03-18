def solution(number, limit, power):
    solider_list = []

    for solider in range(1, number+1):
        if countDenominator(solider) > limit:
            solider_list.append(power)
        else:
            solider_list.append(countDenominator(solider))
    
    return sum(solider_list)

def countDenominator(num):
    cnt = 0

    if num == 2 or num == 3:
        return 2

    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            cnt += 1
    cnt *= 2

    if int(num**0.5) == num**0.5:
        cnt -= 1
    
    return cnt