def game(idx, b):
    start = idx
    for i in range(H):
        if idx<N and b[i][idx] == True:
            idx += 1
        elif idx>0 and b[i][idx-1] == True:
            idx -= 1
    if start == idx:
        return True
    return False

def simul_game(b):
    for i in range(N):
        if not game(i, b):
            return False
    return True

def bt(cnt, board, row):
    global maxim
    if cnt>3:
        return

    if maxim <= cnt:
        return

    if simul_game(board):
        maxim = min(maxim, cnt)
        return



    for j in range(row, H): # row
        for i in range(N-1): # col
            if board[j][i] == False and (i==0 or board[j][i-1] == False) and (i==N-1 or board[j][i+1] == False):
                    board[j][i] = True
                    bt(cnt+1, board, j)
                    board[j][i] = False


N, M, H = map(int, input().split())
board = [[False]*N for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = True
maxim = int(1e9)
bt(0, board, 0)
if maxim == int(1e9):
    print(-1)
else:
    print(maxim)