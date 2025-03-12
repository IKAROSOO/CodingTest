def solution(board, moves):
    bucket = []
    cnt = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(bucket) >= 2:
            if bucket[-2] == bucket[-1]:
                bucket.pop()
                bucket.pop()
                cnt += 2
    
    return cnt