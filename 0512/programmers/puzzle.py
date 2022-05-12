from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

puzzle = []

def checkout(row, col):
    global N
    if row<0 or col<0 or row>=N or col>=N:
        return True
    return False

def bfs(start, b, number):
    queue = deque([])
    queue.append(start)
    reserve = [start]
    b[start[0]][start[1]] = 2

    while queue:
        now = queue.popleft()

        for k in range(4):
            drow, dcol = now[0] + dx[k], now[1] + dy[k]
            if not checkout(drow, dcol) and b[drow][dcol] == number:
                reserve.append((drow, dcol))
                queue.append((drow, dcol))
                b[drow][dcol] = 2

    # (0,0) 기준으로 변경
    for idx in range(len(reserve)):
        row, col = reserve[idx]
        row, col = row - start[0], col - start[1]
        reserve[idx] = (row, col)

    return reserve

def turn(board):
    return list(map(list, zip(*board[::-1])))

def solution(game_board, table):
    global N
    N = len(game_board)
    answer = 0

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                puzzle.append(bfs((i, j), table, 1))

    board = [a[:] for a in game_board]
    for k in range(4):
        board = turn(board)
        print(board)
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    res = bfs((i, j), board, 0)
                    if res in puzzle:
                        puzzle.remove(res)
                        answer += len(res)
                    else:
                        for r, c in res:
                            board[i+r][j+c] = 0



    return answer

print(solution(
[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],
[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
))