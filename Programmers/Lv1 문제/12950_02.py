def solution(arr1, arr2):
    '''주어진 두 행렬의 같은 위치의 원소끼리 더해서 새로운 행렬을 반환하는 함수를 작성'''

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]
    
    return arr1