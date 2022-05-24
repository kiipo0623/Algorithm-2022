count = 0
dx = [-1, -1]
dy = [-1, 1]
def check(row, col, n, b):
    # 세로 체크
    for i in range(row):
        if b[i][col] == 1:
            return False

    for k in range(2):
        for i in range(row + 1):
            drow, dcol = row+(dx[k]*i), col+(dy[k]*i)
            if 0 <= drow < n and 0<= dcol < n:
                if b[drow][dcol] == 1:
                    return False
            else:
                break
    return True

def backtracking(line, cnt, b, n):
    global count
    if cnt == n:
        count+= 1
        return

    for i in range(0, n):
        if check(line, i, n, b):
            b[line][i] = 1
            backtracking(line+1, cnt+1, b, n)
            b[line][i] = 0

def solution(n):
    global count
    board = [[0]*n for _ in range(n)]
    backtracking(0, 0, board, n)
    return count

print(solution(10))