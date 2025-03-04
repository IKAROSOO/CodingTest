def solution(keyinput, board):
    row, col = board[0] // 2, board[1] // 2
    row_loc, col_loc = 0, 0

    direction = {
        "left" : (-1, 0),
        "right" : (1, 0),
        "up" : (0, 1),
        "down" : (0, -1)
    }

    for order in keyinput:
        dx, dy = direction[order]
        next_row, next_col = row_loc + dx, col_loc + dy

        if -row <= next_row <= row and -col <= next_col <= col:
            row_loc, col_loc = next_row, next_col
        
    
    return [row_loc, col_loc]