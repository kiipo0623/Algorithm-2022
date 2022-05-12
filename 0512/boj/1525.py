import sys
sys.setrecursionlimit(10**6)
board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ANS = '123456780'
def checkout(row, col):
    if row<0 or col<0 or row>=3 or col>=3:
        return True
    return False

def make_str(b):
    res = ''
    for i in range(3):
        tmp = map(str, b[i])
        res += ''.join(tmp)
    return res

def dfs(now, visited, cnt, b):
    flag = False
    for k in range(4):
        drow, dcol = now[0] + dx[k], now[1] + dy[k]
        if not checkout(drow, dcol):
            tmp_board = [a[:] for a in b]
            tmp_board[now[0]][now[1]], tmp_board[drow][dcol] = tmp_board[drow][dcol], tmp_board[now[0]][now[1]]
            if make_str(tmp_board) not in visited:
                if make_str(tmp_board) == ANS:
                    return cnt+1
                else:
                    flag = True
                    visited.append(make_str(tmp_board))
                    dfs([drow, dcol], visited, cnt+1, tmp_board)
                    visited.pop()

    if flag == False:
        return

for _ in range(3):
    board.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            start = [i, j]

s = make_str(board)
if s == ANS:
    print(0)
    exit()
answer = int(1e9)
sol = dfs(start, [s], 0, board)

if sol:
    answer = min(answer, sol)

if answer == int(1e9):
    print(-1)
else:
    print(answer)