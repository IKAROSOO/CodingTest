def solution(numbers):
    '''주어진 숫자 배열에서 서로 다른 두 숫자를 더하여
    만들 수 있는 모든 가능한 합계를 오름차순으로 정렬된 배열로 반환'''

    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    return sorted(list(set(answer)))