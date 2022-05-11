from collections import deque
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkout(r, c):
    global N
    if r<0 or c<0 or r>=N or c>=N:
        return True
    return False

def rotate90(board):
    return list(map(list, zip(*board[::-1])))

def check_in(startrow, startcol, row_size, col_size, game_board, tmp_board):
    for x in range(row_size):
        for y in range(col_size):
            if tmp_board[x][y]:
                if game_board[startrow+x][startcol+y] != 0:
                    return False
                for k in range(4):
                    drow, dcol = x+dx[k], y+dy[k]
                    if checkout(drow+startrow, dcol+startcol): # 아예 벗어나는 경우
                        continue
                    else:
                        if 0<=drow<row_size and 0<=dcol<col_size and tmp_board[drow][dcol] == 1: # 원래 1이어야되는곳(나중에 점검)
                            continue
                        else: # 원래 0이어야 되는 곳
                            if game_board[drow+startrow][dcol+startcol] == 1:
                                continue
                            else:
                                return False
    return True



def fill_board(game_board, tmp_board, row_size, col_size):
    # 전체 4 for문 (회전)
    # game board의 0,0부터 크기 가능할때까지
    for k in range(4):
        tmp_board = rotate90(tmp_board)

        for i in range(N-row_size):
            for j in range(N-col_size):
                if check_in(i, j, row_size, col_size, game_board, tmp_board): # 성공 하면
                    print(i, j, "yes")
                    return True



# visit체크 조건 체크
def bfs_puzzle(game_board, row, col, board):
    global N
    MIN_ROW, MIN_COL, MAX_ROW, MAX_COL = row, col, row, col
    visited = [[0]*N for _ in range(N)]
    visited[row][col] = 1
    queue = deque([(row, col)])

    while queue:
        now_row, now_col = queue.popleft()
        if now_row<MIN_ROW: MIN_ROW = now_row
        if now_row>MAX_ROW: MAX_ROW = now_row
        if now_col<MIN_COL: MIN_COL = now_col
        if now_col>MAX_COL: MAX_COL = now_col

        for k in range(4):
            drow, dcol = now_row+dx[k], now_col+dy[k]
            if not checkout(drow, dcol) and board[drow][dcol] == 1 and visited[drow][dcol] == False:
                queue.append((drow, dcol))
                visited[drow][dcol] = 1

    print(MAX_ROW, MIN_ROW, MAX_COL, MIN_COL)
    # 완성 : game board에서 확인
    row_size, col_size = MAX_ROW-MIN_ROW+1, MAX_COL-MIN_COL+1
    print(row_size, now_col)

    tmp_board = [[0]*col_size for _ in range(row_size)]
    for i in range(row_size):
        for j in range(col_size):
            tmp_board[i][j] = visited[MIN_ROW+i][MIN_COL+j]

    # 빼오기 완료

    print(tmp_board)
    fill_board(game_board, tmp_board, row_size, col_size)


def solution(game_board, table):
    global N
    answer = -1
    N = len(game_board)

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                bfs_puzzle(game_board, i, j, table)
                # 발굴해서 확인
                # -1로 채움
    return answer


print(solution(
[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
))