from collections import deque
INF = int(1e9)
# 좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
Board = []

def checkout(row, col):
    global N
    return row<0 or col<0 or row>=N or col>=N

# 이동했을 때의 좌표
def move(pos1, pos2):
    res = []
    global Board
    # 네방향 이동
    for k in range(4):
        new1_x, new1_y = pos1[0]+dx[k], pos1[1]+dy[k]
        new2_x, new2_y = pos2[0]+dx[k], pos2[1]+dy[k]

        if not checkout(new1_x, new1_y) and not checkout(new2_x, new2_y):
            if Board[new1_x][new1_y] == 0 and Board[new2_x][new2_y] == 0:
                res.append([(new1_x, new1_y), (new2_x, new2_y)])

    # 원래 가로인 경우
    if pos1[0] == pos2[0]:
        for k in (1, 3):
            new1_x, new1_y = pos1[0] + dx[k], pos1[1] + dy[k] # 첫번째에서 바뀐거
            new2_x, new2_y = pos2[0] + dx[k], pos2[1] + dy[k] # 두번째에서 바뀐거
            if not checkout(new1_x, new1_y) and not checkout(new2_x, new2_y):
                if Board[new1_x][new1_y] == 0 and Board[new2_x][new2_y] == 0:
                    res.append(sorted([(new1_x, new1_y), (pos1[0], pos1[1])]))
                    res.append(sorted([(new2_x, new2_y), (pos2[0], pos2[1])]))
    # 원래 세로인 경우
    if pos1[1] == pos2[1]:
        for k in (0, 2):
            new1_x, new1_y = pos1[0] + dx[k], pos1[1] + dy[k]  # 첫번째에서 바뀐거
            new2_x, new2_y = pos2[0] + dx[k], pos2[1] + dy[k]  # 두번째에서 바뀐거
            if not checkout(new1_x, new1_y) and not checkout(new2_x, new2_y):
                if Board[new1_x][new1_y] == 0 and Board[new2_x][new2_y] == 0:
                    res.append(sorted([(new1_x, new1_y), (pos1[0], pos1[1])]))
                    res.append(sorted([(new2_x, new2_y), (pos2[0], pos2[1])]))

    return res


# N=5
# Board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
# print(move((0, 1), (1, 1)))

def bfs():
    visited_right = [[INF]*N for _ in range(N)] # (N-1, N-2)
    visited_down = [[INF]*N for _ in range(N)] # (N-2, N-1)
    queue = deque()
    queue.append([(0, 0), (0, 1), 0])
    visited_right[0][0] = 0

    while queue:
        now1, now2, cnt = queue.popleft()
        # 모든 이동에 대해서 시간을 갱신하는 경우만
        for new1, new2 in move(now1, now2):
            # 가로인 경우
            if new1[0] == new2[0]:
                if visited_right[new1[0]][new1[1]] > cnt+1:
                    visited_right[new1[0]][new1[1]] = cnt+1
                    queue.append([new1, new2, cnt+1])
            elif new1[1] == new2[1]:
                if visited_down[new1[0]][new1[1]] > cnt+1:
                    visited_down[new1[0]][new1[1]] = cnt+1
                    queue.append([new1, new2, cnt+1])

    return min(visited_right[N-1][N-2], visited_down[N-2][N-1])

def solution(board):
    global N, Board
    N = len(board)
    Board = [a[:] for a in board]
    return bfs()


print(solution(
[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
))