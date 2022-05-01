# print(list(map(list, zip(*tmp[::-1]))))

def fly_fishbool():
    global board
    tmp_board = []
    N = len(board)
    # 한번 자르기
    cut_front = board[:int(N/2)]
    cut_front.reverse()
    cut_back = board[int(N/2):]
    tmp_board.append(cut_front)
    tmp_board.append(cut_back)
    board = [a[:] for a in tmp_board]

    # 두번 자르기
    tmp_board, left_board = [], []
    for i in range(2):
        t, l = [], []
        for j in range(N//2):
            if i<N//4 and j<N//4:
                t.append(board[i][j])
            else:
                l.append(board[i][j])
        tmp_board.append(t)
        left_board.append(l)
    print(tmp_board)
    print(left_board)

    # 돌리기
    rotate1 = list(map(list, zip(*tmp_board[::-1])))
    rotate2 = list(map(list, zip(*rotate1[::-1])))

    # 붙이기
    new_board = []
    for i in range(len(rotate2)):
        new_board.append(rotate2[i])
    for i in range(len(left_board)):
        new_board.append(left_board[i])

    board = [a[:] for a in new_board]


board = [9, 10, 5, 5, 6, 3, 10, 8]
fly_fishbool()