def solution(arr1, arr2):
    '''주어진 두 행렬의 같은 위치의 원소끼리 더해서 새로운 행렬을 반환하는 함수를 작성'''

    answer = []
    col = len(arr1)
    row = len(arr1[0])

    for i in range(col):
        col_arr = []
        for j in range(row):
            res = arr1[i][j] + arr2[i][j]
            col_arr.append(res)
        answer.append(col_arr)
    
    return answer