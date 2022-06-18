from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def checkout(r, c):
    return r<0 or c<0 or r>=R or c>=C

def find_cheese(r, c):
    q = deque()
    q.append((r, c))
    cache = deque()
    cache.append((r, c))
    visited = [[0 for _ in range(C)] for _ in range(R)]
    visited[r][c] = 1

    while q:
        row, col = q.popleft()
        for k in range(4):
            drow, dcol = row+dx[k], col+dy[k]
            if not checkout(drow, dcol) and visited[drow][dcol] == 0 and board[drow][dcol] == 0:
                if drow == 0 or dcol == 0 or drow == R or dcol == C:
                    return deque()

                visited[drow][dcol] = 1
                q.append((drow, dcol))
                cache.append((drow, dcol))

    return cache

def solution():
    time = 1

    beforecnt = 0
    for i in range(R):
        beforecnt += board[i].count(1)

    if beforecnt == 0:
        print(0)
        print(0)
        return

    while True:
        # 구멍 제거
        rm_list = []
        for head in cheesehead.keys():
            # 여전히 구멍이면
            if len(find_cheese(head[0], head[1])):
                continue
            # 구멍 아니면
            else:
                for c_row, c_col in cheesehead[head]:
                    board[c_row][c_col] = 0
                rm_list.append(head)

        for rm_item in rm_list:
            del cheesehead[rm_item]

        # 치즈 탐색
        cnt = beforecnt
        rm_board = []
        for i in range(R):
            for j in range(C):
                if board[i][j] == 1:
                    for k in range(4):
                        dr, dc = i+dx[k], j+dy[k]
                        if not checkout(dr, dc) and board[dr][dc] == 0:
                            rm_board.append((i, j))
                            break

        cnt -= len(rm_board)
        for i, j in rm_board:
            board[i][j] = 0

        if cnt == 0:
            print(time)
            print(beforecnt)
            return

        beforecnt = cnt
        time += 1


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))

cheesehead = dict()

# 치즈 초기화
for i in range(R):
    for j in range(C):
        if (i!=0 and j!=0 and i!=R and j!=C) and board[i][j] == 0:
            hole = find_cheese(i, j)
            if len(hole):
                cheesehead[hole[0]] = hole
            for r, c in hole:
                board[r][c] = 2

solution()


