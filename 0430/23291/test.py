a = [[1,2], [3,4], [5,6]]
tmp = list(map(list, zip(*a[::-1])))
print(tmp)
print(list(map(list, zip(*tmp[::-1]))))
t = list(map(list, zip(*a)))
print(t)
print(t[::-1])

def clockchange(board):
    R, C = len(board), len(board[0])
    tmp_board = [[0]*R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            tmp_board[j][R-i-1] = board[i][j]

    print(tmp_board)

def exclock(board):
    R, C = len(board), len(board[0])
    tmp_board = [[0]*R for _ in range(C)]

    for i in range(R):
        for j in range(C):
            tmp_board[C-j-1][i] = board[i][j]

    print(tmp_board)
clockchange(a)
exclock(a)