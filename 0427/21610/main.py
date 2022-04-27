direct = {1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def simulate():
    global cloud, board
    for mv in move:

        # 모두 이동 방향으로 이동. cloud 큐 갱신
        d, s = mv
        movedcloud = []
        for c in cloud:
            row, col = c
            drow, dcol = (row + direct[d][0]*s)%N, (col + direct[d][1]*s)%N
            movedcloud.append((drow, dcol))
            board[drow][dcol] += 1

        # 복사 버그 준비
        bugqueue = []
        for m in movedcloud:
            row, col = m
            cnt = 0
            for k in [2, 4, 6, 8]:
                drow, dcol = row + direct[k][0], col + direct[k][1]
                if checkout(drow, dcol):
                    continue
                if board[drow][dcol] > 0:
                    cnt += 1

            bugqueue.append((row, col, cnt))

        #물복사 버그
        for row, col, cnt in bugqueue:
            board[row][col] += cnt

        # 구름 생성
        raincloud = []
        for i in range(N):
            for j in range(N):
                if board[i][j] >= 2 and (i, j) not in movedcloud:
                    raincloud.append((i, j))
                    board[i][j] -= 2

        # 후처리
        cloud = raincloud[:]


N, M = map(int, input().split())
board = []
move = []
cloud = [(N-2, 0), (N-2, 1), (N-1, 0), (N-1, 1)]
answer = 0

for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(M):
    move.append(list(map(int, input().split())))

simulate()

for i in range(N):
    answer += sum(board[i])
print(answer)