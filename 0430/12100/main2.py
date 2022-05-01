# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def checkout(row, col):
    if row<0 or col<0 or row>=N or col>=N:
        return True
    return False
def simulate(dir):
    global board, N
    flagboard = [[False] * N for _ in range(N)]  # 턴마다 갱신
    # 상
    if dir == 0:
        for col in range(N):
            for row in range(1, N):
                value = board[row][col]

                if value == 0:
                    continue

                idx = row
                sumflag = False

                # 탐색 진행
                while True:
                    if checkout(idx-1, col):
                        break
                    if board[idx-1][col] == 0:
                        idx -= 1
                    elif board[idx-1][col] == value and not flagboard[idx-1][col]:
                        idx -= 1
                        sumflag = True
                        break
                    else:
                        break

                # 합치기 진행
                if sumflag == True:
                    board[idx][col] = value+value
                    board[row][col] = 0
                    flagboard[idx][col] = True

                else:
                    board[row][col] = 0
                    board[idx][col] = value


    # 하
    if dir == 1:
        for col in range(N):
            for row in range(N-2, -1, -1):
                value = board[row][col]

                if value == 0:
                    continue

                idx = row
                sumflag = False

                # 탐색 진행
                while True:
                    if checkout(idx+1, col):
                        break
                    if board[idx+1][col] == 0:
                        idx += 1
                    elif board[idx+1][col] == value and not flagboard[idx+1][col]:
                        idx += 1
                        sumflag = True
                        break
                    else:
                        break

                # 합치기 진행
                if sumflag == True:
                    board[idx][col] = value+value
                    board[row][col] = 0
                    flagboard[idx][col] = True

                else:
                    board[row][col] = 0
                    board[idx][col] = value


    # 좌
    if dir == 2:
        for row in range(N):
            for col in range(1, N):
                value = board[row][col]

                if value == 0:
                    continue

                idx = col
                sumflag = False

                # 탐색 진행
                while True:
                    if checkout(row, idx-1):
                        break
                    if board[row][idx-1] == 0:
                        idx -= 1
                    elif board[row][idx-1] == value and not flagboard[row][idx-1]:
                        idx -= 1
                        sumflag = True
                        break
                    else:
                        break

                # 합치기 진행
                if sumflag == True:
                    board[row][idx] = value+value
                    board[row][col] = 0
                    flagboard[row][idx] = True

                else:
                    board[row][col] = 0
                    board[row][idx] = value


    # 우
    if dir == 3:
        for row in range(N):
            for col in range(N-2, -1, -1):
                value = board[row][col]

                if value == 0:
                    continue

                idx = col
                sumflag = False

                # 탐색 진행
                while True:
                    if checkout(row, idx+1):
                        break
                    if board[row][idx+1] == 0:
                        idx += 1
                    elif board[row][idx+1] == value and not flagboard[row][idx+1]:
                        idx += 1
                        sumflag = True
                        break
                    else:
                        break

                # 합치기 진행
                if sumflag == True:
                    board[row][idx] = value+value
                    board[row][col] = 0
                    flagboard[row][idx] = True

                else:
                    board[row][col] = 0
                    board[row][idx] = value



def dfs(cnt):
    global a, ans
    if cnt == 5:
        for i in range(N):
            for j in range(N):
                ans = max(ans, a[i][j])
        return

    temp_a = copy.deepcopy(a)
    for i in range(4):
        move(i)
        dfs(cnt+1)
        a = copy.deepcopy(temp_a)