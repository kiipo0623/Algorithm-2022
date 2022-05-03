from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def checkout(row, col, board):
    if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col] == 0:
        return True
    return False

def bfs(sr, sc, er, ec, board):
    visit = [[0]*len(board[0]) for _ in range(len(board))]
    queue = deque([])
    queue.append([sr, sc])

    while queue:
        nr, nc = queue.popleft()
        for k in range(4):
            drow, dcol = nr+dx[k], nc+dy[k]
            if not checkout(drow, dcol) and not visit[drow][dcol]:
                visit[drow][dcol] = visit[nr][nc]+1
                queue.append([drow, dcol])




def bt(cnt, winner, turn, location, board):
    global answer
    r, c = location[turn]
    if board[r][c] == 0:
        answer = min(answer, cnt)

    # 승자면 가장 가까운 거리 패자면 가장 먼 거리
    for k in range(4):
        drow, dcol = r + dx[k], c + dy[k]



t
def solution(board, aloc, bloc):
    global answer
    answer = -1


    return answer