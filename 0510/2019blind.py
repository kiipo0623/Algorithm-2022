from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def checkout(row, col):
    global N
    if row<0 or col<0 or row>=N or col>=N:
        return True
    return False

def solution(board):
    global N
    answer = 0
    N = len(board)

    def upcheck(row, col):
        for i in range(row):
            if board[i][col] != 0: # -1도 있는거니까 결국
                return False
        return True

    def makevisited(visitpos, fill):
        for r, c in visitpos:
            board[r][c] = fill

    def search(row, col):
        visitpos = []
        LEFT, RIGHT, UP, DOWN = col, col, row, row
        queue = deque()
        queue.append((row, col))
        visitpos.append((row, col))
        number = board[row][col]

        while queue:
            r, c = queue.popleft()
            if r<UP: UP = r
            if r>DOWN: DOWN = r
            if c<LEFT: LEFT = c
            if c>RIGHT: RIGHT = c

            for k in range(4):
                dr, dc = r+dx[k], c+dy[k]
                if not checkout(dr, dc) and board[dr][dc] == number and (dr, dc) not in visitpos:
                    queue.append((dr, dc))
                    visitpos.append((dr, dc))

        flag = True
        for i in range(UP, DOWN+1):
            for j in range(LEFT, RIGHT+1):
                if board[i][j] == number:
                    continue
                else:
                    if board[i][j] != 0: #-1이라도 뭔가 채워져 있으면
                        # 해당블록도 검색해서 검거해서 제거해야함 동시에 (얽혀 있는 경우)
                        continue
                    elif not upcheck(i, j):
                        flag = False
                        break


        if flag == True:
            makevisited(visitpos, 0)
            return 1
        else:
            makevisited(visitpos, -1)
            return 0

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                answer += search(i, j)

    print(board)

    return answer

print(solution(
[[0,0,0,0,0,0,0,0,0,0]
,[0,0,0,2,2,0,0,0,0,0]
,[0,0,0,2,1,0,0,0,0,0]
,[0,0,0,2,1,0,0,0,0,0]
,[0,0,0,0,1,1,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0]]
))