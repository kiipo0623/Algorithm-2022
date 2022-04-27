dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def bt(flag, visit, cnt, row, col, height):
    global answer
    small, kill = [], []

    for i in range(4):
        drow, dcol = row+dx[i], col+dy[i]

        if checkout(drow, dcol): # 삐져나감
            continue
        if (drow, dcol) in visit: # 이미 방문함
            continue

        if board[drow][dcol] < height: # 더 작은경우 그냥 카운트
            small.append((drow, dcol))

        elif board[drow][dcol]-K < height: # 뺄수 있는경우 :
            mink = K
            for i in range(K, 0, -1):
                if board[drow][dcol]-i <height:
                    mink = i

            kill.append((drow, dcol, mink))

    if len(small) == 0:
        if flag or len(kill) == 0:
            answer = max(answer, cnt)
            return

    if flag == False:
        for r, c, k in kill:
            for i in range(k, K+1):
                visit.append((r,c))
                bt(True, visit, cnt+1, r, c, board[r][c]-i)
                visit.pop()

    for r, c in small:
        visit.append((r, c))
        bt(flag, visit, cnt+1, r, c, board[r][c])
        visit.pop()

# import sys
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

    # print("start", start)
    for r, c in start:
        bt(False, [(r, c)], 1, r, c, high)

    print("#%d %d"%(t, answer))