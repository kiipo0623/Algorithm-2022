def rotate(b):
    return list(map(list, zip(*b[::-1])))

# 모든 칸을 다 채웠는지
def check(r, c):
    global N, M, board, newkey, empty
    cnt = 0
    for i in range(M):
        for j in range(M):
            if board[i+r][j+c] == -1:
                continue
            elif board[i+r][j+c] == newkey[i][j]:
                return False
            elif board[i+r][j+c] == 0:
                cnt += 1
    if cnt == empty:
        return True
    else:
        return False

def solution(key, lock):
    global N, M, board, newkey, empty
    N, M = len(lock), len(key)
    empty = 0
    for i in range(N):
        empty += lock[i].count(0)

    board = [[-1]*(N+M+M) for _ in range(N+M+M)]

    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]

    newkey = [a[:] for a in key]

    for k in range(4):
        newkey = rotate(newkey)
        for row in range(1, M+N):
            for col in range(1, M+N):
                if check(row, col):
                    return True
    return False

print(solution(
[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
))

# print(rotate(
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# ))