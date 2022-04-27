dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def bt(visitplace, visitdessert, dir, cnt):
    global answer
    # print("visitplace")
    # print(visitplace)
    if visitplace[-1][0] == visitplace[0][0] and visitplace[-1][1] == visitplace[0][1] and cnt >= 4: # 사각형인지 검증을 안한다
        answer = max(answer, cnt)
        return

    row, col = visitplace[-1][0], visitplace[-1][1]
    testlist = []

    if dir == 0:
        if cnt == 0: # 처음인 경우
            testlist = [0]
        else:
            testlist = [0, 1]

    if dir == 1:
        testlist = [1, 2]
    if dir == 2:
        testlist = [2, 3]
    if dir == 3:
        testlist = [3]

    for tmpdir in testlist:
        drow, dcol = row+dx[tmpdir], col+dy[tmpdir]
        if (not checkout(drow, dcol)) and ((drow, dcol) not in visitplace[1:]) and (board[drow][dcol] not in visitdessert[1:]):
            visitplace.append((drow, dcol))
            visitdessert.append(board[drow][dcol])
            bt(visitplace, visitdessert, tmpdir, cnt+1)
            visitplace.pop()
            visitdessert.pop()


def simulate(board):
    for i in range(N):
        for j in range(N):
            bt([(i, j)], [board[i][j]], 0, 0)

# import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
for t in range(1, T+1):
    answer = -1
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    simulate(board)
    print("#{} {}".format(t, answer))