# 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def find(s,b):
    for i in range(N):
        for j in range(M):
            if b[i][j] == s:
                return i, j

def bt(b, cnt, visit):
    global answer
    if cnt >= answer:
        return

    save = [a[:] for a in b]
    r_row, r_col = find('R', b)
    b_row, b_col = find('B', b)

    for i in range(4):
        r_mvcnt, b_mvcnt = 0, 0
        redflag, blueflag = False, False
        r_drow, r_dcol, b_drow, b_dcol = r_row, r_col, b_row, b_col

        while True:
            # 빨간색에 대해서
            r_drow += dx[i]
            r_dcol += dy[i]
            r_mvcnt += 1
            if b[r_drow][r_dcol] == 'O':
                redflag = True
                break
            elif b[r_drow][r_dcol] == '#':
                r_drow, r_dcol = r_drow - dx[i], r_dcol - dy[i]
                break

        while True:
            # 파란색에 대해서
            b_drow += dx[i]
            b_dcol += dy[i]
            b_mvcnt += 1
            if b[b_drow][b_dcol] == 'O':
                blueflag = True
                break
            elif b[b_drow][b_dcol] == '#':
                b_drow, b_dcol = b_drow - dx[i], b_dcol - dy[i]
                break

        # 파랑만 빠질 수 있음, 둘다 빠지는 경우 포함 실패
        if blueflag:
            continue

        # 빨강만 빠질 수 있음
        if redflag and not blueflag:
            answer = min(answer, cnt)
            continue

        # 두 곳이 겹칠 수 있음
        if r_drow == b_drow and r_dcol == b_dcol:
            if r_mvcnt < b_mvcnt: # 한칸 물림
                b_drow, b_dcol = b_drow - dx[i], b_dcol - dy[i]

            elif r_mvcnt > b_mvcnt:
                r_drow, r_dcol = r_drow - dx[i], r_dcol - dy[i]

        if (r_drow, r_dcol, b_drow, b_dcol) in visit:
            continue

        # 안빠지는 경우 백트래킹
        b[r_row][r_col] = '.'
        b[b_row][b_col] = '.'
        b[r_drow][r_dcol] = 'R'
        b[b_drow][b_dcol] = 'B'
        visit.append((r_drow, r_dcol, b_drow, b_dcol))
        bt(b, cnt+1, visit)

        b = [s[:] for s in save]
        visit.pop()




N, M = map(int, input().split())
board = []
red_row, red_col, blue_row, blue_col, hole_row, hole_col = 0, 0, 0, 0, 0, 0
answer = 11
for i in range(N):
    data = list(input())
    for j in range(M):
        if data[j] == 'O':
            hole_row, hole_col = i, j
        elif data[j] == 'R':
            red_row, red_col = i, j
        elif data[j] == 'B':
            blue_row, blue_col = i, j
    board.append(data)
bt(board, 1, [(red_row, red_col, blue_row, blue_col)])
if answer == 11:
    print(-1)
else:
    print(answer)
