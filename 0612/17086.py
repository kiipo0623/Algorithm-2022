from collections import deque
N, M = map(int, input().split())
board = []
shark_loc = []
mv = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for i in range(N):
    t = list(map(int, input().split()))
    for j in range(M):
        if t[j] == 1:
            shark_loc.append((0, i, j))
    board.append(t)

shark_loc = deque(shark_loc)
visited = [[0 for _ in range(M)] for _ in range(N)]

while shark_loc:
    dist, r, c = shark_loc.popleft()
    for dr, dc in mv:
        drow, dcol = r+dr, c+dc
        if 0<=drow<N and 0<=dcol<M:
            if board[drow][dcol] == 1:
                continue
            if visited[drow][dcol] == 0:
                visited[drow][dcol] = dist+1
                shark_loc.append((dist+1, drow, dcol))

answer = 0
for i in range(N):
    answer = max(answer, max(visited[i]))
print(answer)