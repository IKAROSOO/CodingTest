import re

def solution(dartResult):
    '''다트 게임에서 얻은 점수와 영역(S, D, T), 옵션(*, #)을 조합하여 총 점수를 계산하는 함수를 작성'''
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'*': 2, '#': -1, '': 1}
    p = re.compile('([0-9]{1,2})([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] = (dart[i-1][0], dart[i-1][1], dart[i-1][2]+'*')
    score = []
    for s, b, o in dart:
        score.append(int(s)**bonus[b] * option[o])
    return sum(score)