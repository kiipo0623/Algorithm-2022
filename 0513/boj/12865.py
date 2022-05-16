N, K = map(int, input().split())
# 기준 : 무게 [0]가치 [1]방문여부
board = [[0, 0] for _ in range(K+1)]
item = dict()

for i in range(N):
    W, V = map(int, input().split())
    if W <= K and V > board[W][0]:
        board[W][0] = V
        board[W][1] = 1<<i
    item[i] = [W, V]

# 무게 순서대로 탐색
for i in range(K+1):
    if board[i][0] == 0:
        continue

    # 아이템 순서대로 탐색
    for j in range(N):
        if (board[i][1]&1<<j) == 0: # 방문하지 않았으면
            val = board[i][0] + item[j][1]
            wei = i + item[j][0]
            visit = board[i][1] | 1<<j
            if wei > K:
                continue
            if (board[wei][1] & visit == 0) and (board[wei][0] <= val):
                board[wei][1] = visit
                board[wei][0] = val
MAX = 0
for i in range(K+1):
    if board[i][0] > MAX: MAX = board[i][0]
print(MAX)

