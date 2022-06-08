dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def A_turn(a_row, a_col, b_row, b_col, state, cnt):
    if state[a_row][a_col] == 0:
        return (True, cnt) # 니가 이겼을 때 True return

    winlst, loselst, flag = [], [], False

    for k in range(4):
        drow, dcol = a_row+dx[k], a_col+dy[k]
        if 0<=drow<len(state) and 0<=dcol<len(state[0]) and state[drow][dcol] == 1: # 갈 수 있는 경우
            flag = True
            s = [st[:] for st in state]
            s[a_row][a_col] = 0
            isWin, count = B_turn(b_row, b_col, drow, dcol, s, cnt+1)

            if isWin: # 내가 승리
                winlst.append(count)
            else:
                loselst.append(count)

    # 과정 다끝나고 나서
    if flag:
        if winlst:
            return (False, min(winlst))
        else:
            return (True, max(loselst))
    else:
        return (True, cnt)


def B_turn(b_row, b_col, a_row, a_col, state, cnt):
    if state[b_row][b_col] == 0:
        return (True, cnt)

    winlst, loselst, flag = [], [], False

    for k in range(4):
        drow, dcol = b_row+dx[k], b_col+dy[k]
        if 0<=drow<len(state) and 0<=dcol<len(state[0]) and state[drow][dcol] == 1:
            flag = True
            s = [st[:] for st in state]
            s[b_row][b_col] = 0
            isWin, count = A_turn(a_row, a_col, drow, dcol, s, cnt+1)

            if isWin:
                winlst.append(count)
            else:
                loselst.append(count)

    if flag:
        if winlst:
            return (False, min(winlst))
        else:
            return (True, max(loselst))
    else:
        return (True, cnt)

def solution(board, aloc, bloc):
    answer = A_turn(aloc[0], aloc[1], bloc[0], bloc[1], board, 0)[1]
    return answer


print(solution(
[[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1,0], [1,2]
))