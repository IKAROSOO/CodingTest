def solution(ingredients):
    cnt = 0
    burgerStack = []

    for ingredient in ingredients:
        burgerStack.append(ingredient)
        
        if len(burgerStack) >= 4 and ingredient == 1:
            if burgerStack[-4:] == [1, 2, 3, 1]:
                cnt += 1
                del burgerStack[-4:]
    
    return cnt