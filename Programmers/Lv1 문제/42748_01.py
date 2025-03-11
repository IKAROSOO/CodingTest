def solution(array, commands):
    '''주어진 배열(array)에서 특정 범위(i~j)를 자르고 정렬한 후,
    그 결과에서 k번째에 있는 수를 찾는 과정을 여러 번 반복하여 결과를 배열로 반환'''

    answer = []

    for command in commands:
        res = array[command[0]-1 : command[1]]
        res.sort()
        answer.append(res[command[2]-1])
    
    return answer