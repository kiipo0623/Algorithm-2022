N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))

def colchecker(b):
    maxim = 1
    for i in range(N):
        before, cnt = b[0][i], 1
        for j in range(1, N):
            if b[j][i] == before:
                cnt += 1
            else:
                maxim = max(maxim, cnt)
                before, cnt = b[j][i], 1
        maxim = max(maxim, cnt)
    return maxim

def rowchecker(b):
    maxim = 1
    for i in range(N):
        before, cnt = b[i][0], 1
        for j in range(1, N):
            if b[i][j] == before:
                cnt += 1
            else:
                maxim = max(maxim, cnt)
                before, cnt = b[i][j], 1
        maxim = max(maxim, cnt)
    return maxim

def solution(board):
    answer = 1
    for i in range(N):
        for j in range(N):
            for d in [(0, 1), (1, 0)]:
                drow, dcol = i+d[0], j+d[1]
                if 0<=drow<N and 0<=dcol<N:
                    tmp = [a[:] for a in board]
                    tmp[i][j], tmp[drow][dcol] = tmp[drow][dcol], tmp[i][j]
                    answer = max(answer, rowchecker(tmp))
                    answer = max(answer, colchecker(tmp))

    return answer

print(solution(board))

