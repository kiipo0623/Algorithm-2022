from collections import deque
def high_fishbool():
    global board
    new_board = []
    a = [board[0]]
    b = board[1:]
    new_board.append(a)
    new_board.append(b)
    board = [n[:] for n in new_board]

    while True:
        height = len(board)
        width = len(board[-1]) - len(board[0])

        if width - height < 0:
            return

        mv_row, mv_col = height, len(board[0])

        # 바꿔야 하는 것 떼어 오기
        tmp = []
        for r in range(mv_row):
            tmp_r = []
            for c in range(mv_col):
                tmp_r.append(board[r][c])
            tmp.append(tmp_r)

        # 떼어 온 것 회전
        rotate = list(map(list, zip(*tmp[::-1])))

        new_board = []
        for i in range(len(rotate)):
            new_board.append(rotate[i])
        new_board.append(board[-1][mv_col:])
        board = [n[:] for n in new_board]

board = [5,3,3,14,9,3,11,8]
# board = [[3,5], [3,14,9,3,11,8]]
high_fishbool()

