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

    true_flag = True
    for i in range(N):
        for j in range(N):
            biglock[N+i][N+j] = lock[i][j]
            if lock[i][j] == 0:
                true_flag = False
                lock_home.append((N+i, N+j))

    if true_flag:
        return True

    HOMENUM = len(lock_home)
    lock_home = lock_home[::-1]
    key_dolge = key_dolge[::-1]

    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_dolge.append((i, j))

    for home_row, home_col in lock_home:
        for key_row, key_col in key_dolge:
            # 여기서 잘못돌림 돌리면 시작하는 srow, scol이 바뀌어야
            t_key = key[:]
            for i in range(4):
                srow, scol = home_row - key_row, home_col - key_col
                if check(srow, scol, biglock, t_key):
                    return True
                # 회전
                t_key = turn(t_key)
                key_row, key_col = key_col, M-key_row-1

    return False

print(solution(
[[0, 0, 0], [1, 0, 0], [0, 1, 1]],
[[1, 1, 1], [1, 1, 0], [1, 0, 1]]
))