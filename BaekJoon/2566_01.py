board = []

for i in range(9):
    board.append(list(map(int, input().split())))

key = int(0)
col = 0
row = 0

for i in range(9):
    for j in range(9):
        if board[i][j] >= key:
            key = board[i][j]
            col = i+1
            row = j+1

print(key)
print(col, row)