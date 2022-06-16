def checkin(r, c):
    if 0<=r<N and 0<=c<N:
        return True
    return False

def backtrack(idx, cnt, b):
    global answer
    if idx == place_cnt:
        answer = max(answer, cnt)
        return

    r, c = place_cand[idx]

    flag = True
    for i in range(1, N):
        if (checkin(r-i, c-i) and b[r - i][c - i] == '2') or \
                (checkin(r+i, c+i) and b[r + i][c + i] == '2') or \
                (checkin(r-i, c+i) and b[r - i][c + i] == '2') or \
                (checkin(r+i, c-i) and b[r + i][c - i]== '2'):
            flag = False
            break

    if flag:
        backup = b[r]
        tmp = b[r][:c] + '2' + b[r][c+1:]
        b[r] = tmp
        backtrack(idx+1, cnt+1, b)
        b[r] = backup

    # 해당 위치에 안놓는 경우는 무조건 가능
    backtrack(idx+1, cnt, b)


N = int(input())
place_cand = []
board = []
place_cnt = 0
answer = 0
for i in range(N):
    tmp = list(map(str, input().split()))
    board.append(''.join(tmp))
    for j in range(N):
        if tmp[j] == '1':
            place_cnt += 1
            place_cand.append((i, j))

backtrack(0, 0, board)
print(answer)

