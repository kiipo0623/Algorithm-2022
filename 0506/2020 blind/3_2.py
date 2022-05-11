def turn(key):
    return list(map(list, zip(*key[::-1])))

def check(srow, scol, biglock, tmp_key):
    global N, M, HOMENUM
    counter = 0
    for i in range(M):
        for j in range(M):
            if biglock[srow+i][scol+j] in [0, 1]:
                if (tmp_key[i][j], biglock[i+srow][j+scol]) == (1, 0):
                    counter += 1
                elif (tmp_key[i][j], biglock[i+srow][j+scol]) == (0, 1):
                    continue
                else:
                    return False
    if counter == HOMENUM:
        return True
    else:
        return False

def solution(key, lock):
    global N,M,HOMENUM
    N, M = len(lock), len(key)
    biglock = [[2]*(3*N) for _ in range(3*N)]

    lock_home = []
    key_dolge = []

    for i in range(N):
        for j in range(N):
            biglock[N+i][N+j] = lock[i][j]
            if lock[i][j] == 0:
                lock_home.append((N+i, N+j))

    HOMENUM = len(lock_home)

    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_dolge.append((i, j))

    for k in range(4):
        for i in range(N-M+1, 2*N):
            for j in range(N-M+1, 2*N):
                if check(i, j, biglock, key):
                    return True
        key = turn(key)

    return False

print(solution(
[[0, 0, 0], [1, 0, 0], [0, 1, 1]],
[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
))