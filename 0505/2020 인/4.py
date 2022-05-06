from collections import deque
# 좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
def checkout(row, col, N):
    if row<0 or col<0 or row>=N or col>=N:
        return True
    return False

def bfs(board):
    N = len(board)
    INF = int(1e9)

    cost = [[INF]*N for _ in range(N)]
    cost[0][0] = 0
    queue = deque([])
    if not board[0][1]:
        cost[0][1] = 100
        queue.append([0, 1, 2, 100])
    if not board[1][0]:
        cost[1][0] = 100
        queue.append([1, 0, 1, 100]) # row, col, 이전dir, 이전비용

    while queue:
        row, col, bef_dir, bef_cost = queue.popleft()
        for k in range(4):
            drow, dcol = row+dx[k], col+dy[k]
            if k%2 == bef_dir%2:
                new_cost = bef_cost+100
            else:
                new_cost = bef_cost+600
            if not checkout(drow, dcol, N) and not board[drow][dcol] and cost[drow][dcol] >= new_cost:
                cost[drow][dcol] = new_cost
                queue.append([drow, dcol, k, new_cost])
    return cost[N-1][N-1]


def solution(board):
    return bfs(board)
# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution(
[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
))
print(solution(
[[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]
))