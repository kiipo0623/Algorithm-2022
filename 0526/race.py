from collections import deque

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# visit체크
# 최솟값 안쓰면 > 너무반복됨 (비효율 ~ 시간초과)
# 중간까지는 더 비싸지만 마지막에 더 싸지는 경우 존재해서 오답

def solution(board):
    N = len(board)
    # queue = deque([(1, (0, 1), 1), (2, (1, 0), 1)])
    queue = deque([(1, (0, 0), 0), (2, (0, 0), 0)])
    visit = [[[int(1e9)] * 4 for _ in range(N)] for _ in range(N)]
    # queue = deque()
    # for i in range(4):
    #     visit[0][0][i] = 0
    # if not board[1][0]:
    #     queue.append((2, (1, 0), 1))
    # if not board[0][1]:
    #     queue.append((1, (0, 1), 1))
    # visit체크를 두 방향에 대해서 : 상하 / 좌우


    while queue:
        direct, pos, cost = queue.popleft()
        if visit[pos[0]][pos[1]][direct] > cost:
            visit[pos[0]][pos[1]][direct] = cost
            for k in range(4):
                dx_pos, dy_pos = pos[0]+dx[k], pos[1]+dy[k]
                if 0 <= dx_pos < N and 0 <= dy_pos < N and not board[dx_pos][dy_pos]:
                    if k%2 == direct%2: #방향 같은 경우
                        queue.append((k, (dx_pos, dy_pos), cost+1))

                    else: # 방향 다른 경우
                        queue.append((k, (dx_pos, dy_pos), cost+6))

    ans = int(1e9)
    print(visit)
    for i in range(4):
        ans = min(ans, visit[N-1][N-1][i])
    return ans * 100

print(solution(
[[0,0,0],[0,0,0],[0,0,0]]
))
# print(solution(
# [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# ))
# print(solution(
# [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# ))
# print(solution(
# [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
# ))