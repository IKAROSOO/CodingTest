def solution(board):
    answer = 0
    dangerous = [[0] * len(board) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for x in range(max(0, i-1), min(len(board), i+2)):
                    for y in range(max(0, j-1), min(len(board), j+2)):
                        if 0 <= x < len(board) and 0 <= y <= len(board):
                            dangerous[x][y] = 1
    
    for i in range(len(board)):
        for j in range(len(board)):
            if dangerous[i][j] == 0:
                answer += 1
    
    return answer

# -> 제미나이가 해결