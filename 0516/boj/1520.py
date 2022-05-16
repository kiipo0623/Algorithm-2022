dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 호출할 때 한번만 호출해야 함(아니면 여러번 더해지니까)
# 들어오는 걸 기준으로 해야
def checkout(row, col):
    return row<0 or col<0 or row>=M or col>=N

def dfs(now):
    global count, checkout
    r, c = now
    for k in range(4):
        if checker[r][c][k] == True: # 들어오는 걸 기준으로    ???
            continue
        dr, dc = r+dx[k], c+dy[k]
        if not checkout(dr, dc) and board[dr][dc] < board[r][c]:
            if checker[dr][dc][k]:
                count[dr][dc] += 1
            else:
                count[dr][dc] += count[r][c]
                checker[dr][dc][k] = True
            dfs([dr, dc])


M, N = map(int, input().split())
board = []
count = [[0]*N for _ in range(M)]
count[0][0] = 1
checker = [[[False, False, False, False] for _ in range(N)] for _ in range(M)]
for _ in range(M):
    board.append(list(map(int, input().split())))
dfs([0, 0])
# print(count[M-1][N-1])
# print(count)
# print(checker)