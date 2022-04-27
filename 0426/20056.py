from collections import deque
N, M, K = map(int, input().split())
direction = {0: [-1, 0], 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[1, 0], 5:[1, -1], 6:[0, -1], 7:[-1, -1]}

def new_rc(row, col, dir, speed):
    for s in range(speed):
        drow, dcol = row + direction[dir][0], col + direction[dir][1]
        if drow==-1:
            drow = N-1
        elif drow==N:
            drow = 0
        if dcol==-1:
            dcol = N-1
        elif dcol == N:
            dcol = 0
        row, col = drow, dcol
    return row, col

def move_ball():
    new_board = [[[0] * 3 for _ in range(N)] for _ in range(N)]
    new_cnt_board = [[0] * N for _ in range(N)]
    leng = len(pos_queue)
    for _ in range(leng):
        row, col = pos_queue.popleft()
        m, s, d = board[row][col]
        if cnt_board[row][col] == 1:
            nrow, ncol = new_rc(row, col, d, s)
            if new_cnt_board[nrow][ncol] == 0:
                new_board[nrow][ncol][0] += m
                new_board[nrow][ncol][1] += s
                new_board[nrow][ncol][2] = d
                new_cnt_board[nrow][ncol] += 1
            else: # 두개 이상인 곳
                new_board[nrow][ncol][0] += m
                new_board[nrow][ncol][1] += s
                new_cnt_board[nrow][ncol] += 1
                multi_queue.append([nrow, ncol])
                # 방향 조정
                if new_board[nrow][ncol][2] == 8: # 지금까지 다 짝수
                    new_board[nrow][ncol][2] = 8 if d%2 == 0 else 10
                elif new_board[nrow][ncol][2] == 9: # 지금까지 다 홀수
                    new_board[nrow][ncol][2] = 9 if d%2 == 1 else 10
                elif new_board[nrow][ncol][2] == 10:
                    new_board[nrow][ncol][2] = 10

        elif cnt_board[row][col] == 4:
                for i in range(4):

        else:
            print("error")

def simulate():
    for _ in range(K):
        move_ball()

pos_queue = deque([])
multi_queue = deque([])
board = [[[0]*3 for _ in range(N)] for _ in range(N)]
cnt_board = [[0]*N for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r-1, c-1
    pos_queue.append((r, c))
    board[r][c][0], board[r][c][1], board[r][c][2] = m, s, d
    cnt_board[r][c] += 1

print(board)
print(cnt_board)
print(pos_queue)

