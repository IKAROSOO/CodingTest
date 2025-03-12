def solution(n, lost, reverse):
    '''도난당한 학생과 여벌 옷을 가져온 학생 목록을 활용하여
    최대한 많은 학생이 체육복을 입을 수 있도록 배분'''

    answer = n - len(lost)

    for i in range(len(lost)):
        pas = False
        for gift in reverse:
            print(reverse)
            if abs(lost[i] - gift) <= 1:
                answer += 1
                reverse.remove(gift)
                pas = True
                break
        if pas:
            continue

    return answer

'''
실패
'''