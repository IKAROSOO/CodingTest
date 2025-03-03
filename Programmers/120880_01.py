def solution(numlist, n):
    answer = []
    closeList = []

    for element in numlist:
        closeList.append(abs(element - n))
    
    closeList = remove_duplicates(closeList)
    closeList.sort()

    for element in closeList:
        smaller = n - element
        bigger = n + element

        if element == 0:
            answer.append(n)
            continue

        if smaller in numlist or bigger in numlist:
            if bigger in numlist:
                answer.append(bigger)
                print(answer)                
            if smaller in numlist:
                answer.append(smaller)
                print(answer)

    return answer

def remove_duplicates(my_list):
    return list(set(my_list))