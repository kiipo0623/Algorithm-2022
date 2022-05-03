from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkout(row, col, board):
    if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or not board[row][col]:
        return True
    return False

def bt(cnt, turn, location, board):
    print("--")
    global answer
    r, c = location[turn]
    other_r, other_c = location[(turn+1)%2]

    mvqueue = deque([])
    mvflag = False
    if not board[r][c]:
        answer = min(answer, cnt)
        return

    for k in range(4):
        drow, dcol = r+dx[k], c+dy[k]
        if not checkout(drow, dcol, board):
            mvqueue.append([drow, dcol])
            if drow == other_r and dcol == other_c:
                mvflag = True

    if len(mvqueue) == 0 and mvflag == True:
        answer = min(answer, cnt+1)
        return

    while mvqueue:
        nr, nc = mvqueue.popleft()
        board[r][c] = 0
        location[turn] = [nr, nc]
        bt(cnt+1, (turn+1)%2, location, board)
        board[nr][nc] = 1
        location[turn] = [r, c]


def solution(board, aloc, bloc):
    global answer
    answer = -1
    location = [aloc, bloc]
    bt(0, 0, location, board)
    return answer

print(solution(
[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]
))
