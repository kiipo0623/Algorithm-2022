dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def bt(flag, visit, cnt, row, col, height):
    global answer
    same, small = [], []

    for i in range(4):
        drow, dcol = row+dx[i], col+dy[i]
        if checkout(drow, dcol):
            continue
        if (drow, dcol) in visit:
            continue
        if board[drow][dcol] < height:
            small.append((drow, dcol))
        elif board[drow][dcol] == height:
            same.append((drow, dcol))

    if len(small) == 0:
        if flag or len(same) == 0:
            answer = max(answer, cnt)
            return

    if flag == False:
        for r, c in same:
            for i in range(1, 6):
                visit.append((r,c))
                bt(True, visit, cnt+1, r, c, board[r][c]-i)
                visit.pop()

    for r, c in small:
        visit.append((r, c))
        bt(flag, visit, cnt+1, r, c, board[r][c])
        visit.pop()

import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    board = []
    answer = 0
    high = -1

    for j in range(N):
        data = list(map(int, input().split()))
        if max(data) > high:
            high = max(data)
        board.append(data)

    start = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == high:
                start.append((i, j))

    print("start", start)
    for r, c in start:
        bt(False, [(r, c)], 1, r, c, high)

    print("#%d %d"%(t, answer))