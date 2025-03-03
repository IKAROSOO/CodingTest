def solution(keyinput, board):
    row, col = board[0]//2, board[1]//2
    row_loc, col_loc = 0, 0

    for order in keyinput:
        if order == "left":
            if row_loc > -row:
                row_loc -= 1
        elif order == "right":
            if row_loc < row:
                row_loc += 1
        elif order == "up":
            if col_loc < col:
                col_loc += 1
        elif order == "down":
            if col_loc > -col:
                col_loc -= 1

        print(row_loc, col_loc)
    return [row_loc, col_loc]