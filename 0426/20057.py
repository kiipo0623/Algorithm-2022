from math import floor
direct = [0, 1, 2, 3]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
wind = {0:[(-2, 0, 0.02), (-1, -1, 0.10), (-1, 0, 0.07), (-1, 1, 0.01)],
        1:[(0, -2, 0.02), (1, -1, 0.10), (0, -1, 0.07), (-1, -1, 0.01)],
        2:[(-2, 0, 0.02), (-1, 1, 0.10), (-1, 0, 0.07), (-1, -1, 0.01)],
        3:[(0, -2, 0.02), (-1, -1, 0.10), (0, -1, 0.07), (1, -1, 0.01)]
        }
wind5 = {0:[0, -2], 1: [2, 0], 2:[0, 2], 3:[-2, 0]}


def out(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    else: return False

def sand(srow, scol, dir):
    global board, answer
    # 전처리
    sand_full = board[srow][scol]
    # for alpha
    sand_gone = 0

    # 5% 먼저 처리
    drow, dcol = srow+wind5[dir][0], scol+wind5[dir][1]
    sand_now = floor(sand_full * 0.05)
    sand_gone += sand_now

    if out(drow, dcol):
        answer += sand_now
    else:
        board[drow][dcol] += sand_now
    # 나머지 퍼센트 처리
    for mv_x, mv_y, per in wind[dir]:
        drow, dcol = srow+mv_x, scol+mv_y
        sand_now = floor(sand_full * per)
        sand_gone += sand_now
        if out(drow, dcol):
            answer += sand_now
        else:
            board[drow][dcol] += sand_now

    if dir%2 == 0: # 짝수일때
        for mv_x, mv_y, per in wind[dir]:
            drow, dcol = srow-mv_x, scol+mv_y
            sand_now = floor(sand_full * per)
            sand_gone += sand_now
            if out(drow, dcol):
                answer += sand_now
            else:
                board[drow][dcol] += sand_now
    else:
        for mv_x, mv_y, per in wind[dir]:
            drow, dcol = srow+mv_x, scol-mv_y
            sand_now = floor(sand_full * per)
            sand_gone += sand_now
            if out(drow, dcol):
                answer += sand_now
            else:
                board[drow][dcol] += sand_now


    # 모든 과정 후 알파 처리
    alpha = sand_full - sand_gone
    arow, acol = srow + dx[dir], scol+dy[dir]
    if out(arow, acol):
        answer += alpha
    else:
        board[arow][acol] += alpha
    board[srow][scol] = 0

def simulate():
    global tornado_row, tornado_col
    cnt = 0
    while True:
        if tornado_row == 0 and tornado_col == 0:
            return
        ntime = time[cnt]
        ndir = direct[cnt % 4]
        for t in range(ntime):
            nrow, ncol = tornado_row+dx[ndir], tornado_col+dy[ndir]
            sand(nrow, ncol, ndir)
            tornado_row, tornado_col = nrow, ncol
        cnt += 1

N = int(input())
tornado_row, tornado_col = N//2, N//2
time = []
answer = 0
for i in range(1, N):
    time.append(i)
    time.append(i)
time.append(N-1)

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

simulate()
print(answer)


