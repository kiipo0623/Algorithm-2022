from collections import deque

N = int(input())
board = []
answer = int(1e9)

for _ in range(N):
    board.append(list(map(int, input().split())))

def check(x, y, d1, d2):
    global N
    if x+d1+d2 >= N:
        return False
    if y-d1 < 0 or y + d2 >=N:
        return False
    return True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 마지막으로 포함되는 위치까지
def bfs(n_row, n_col, s_row, s_col, e_row, e_col, idx):
    global filter, people, board
    q = deque()
    q.append((n_row, n_col))

    while q:
        now_row, now_col = q.popleft()
        if now_row < s_row or now_col < s_col or now_row > e_row or now_col > e_col:
            continue
        if filter[now_row][now_col]:
            continue

        filter[now_row][now_col] = True
        people[idx] += board[now_row][now_col]

        for k in range(4):
            d_row, d_col = now_row+dx[k], now_col+dy[k]
            q.append((d_row, d_col))


def simulate(x, y, d1, d2):
    global N, board, people, filter
    # 필터 설정

    filter = [[False]*N for _ in range(N)]

    people = [0] * 6
    for i in range(d1+1):
        if not filter[y-i][x+i]:
            filter[y-i][x+i] = True
            people[5] += board[y-i][x+i]
        if not filter[y+d2-i][x+d2+i]:
            filter[y+d2-i][x+d2+i] = True
            people[5] += board[y+d2-i][x+d2+i]

    for i in range(d2+1):
        if not filter[y+i][x+i]:
            filter[y+i][x+i] = True
            people[5] += board[y+i][x+i]
        if not filter[y-d1+i][x+d1+i]:
            filter[y-d1+i][x+d1+i] = True
            people[5] += board[y-d1+i][x+d1+i]
    print(filter)

    # 선거구별로 bfs 진행
    # n_row, n_col, s_row, s_col, e_row, e_col, idx
    bfs(0, 0, 0, 0, y, x+d1-1, 1)
    bfs(N-1, 0, y+1, 0, N-1, x+d2, 2)
    bfs(0, N-1, 0, x+d1, y-d1+d2-1, N-1, 3)
    bfs(N-1, N-1, y-d1+d2, x+d2+1, N-1, N-1, 4)

    for i in range(N):
        for j in range(N):
            if not filter[i][j]:
                people[5] += board[i][j]

    print(x, y, d1, d2)
    print(people)
    print("sol ", max(people[1:]) - min(people[1:]))
    return max(people[1:]) - min(people[1:])

simulate(1, 2, 1, 2)

def select():
    global answer
    for x in range(0, N):
        for y in range(1, N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if check(x, y, d1, d2):
                        answer = min(answer, simulate(x, y, d1, d2))


# select()
print(answer)