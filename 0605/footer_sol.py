from copy import deepcopy

def canMove(board, loc):
    r, c = loc
    for idx, (dr, dc) in enumerate([[0,1], [0,-1], [1,0], [-1,0]]):
        nr, nc = r+dr, c+dc
        if ((0<=nr<len(board)) and (0<=nc<len(board[0])) and (board[nr][nc] == 1)):
            return True
    return False

def search(board, aloc, bloc, step):
    if step % 2 == 0:
        r, c = aloc
    else:
        r, c = bloc

    if not board[r][c]:
        return (False, step)

    nboard = deepcopy(board)
    nboard[r][c] = 0
    canWin = False
    maxTurn, minTurn = 0, float('int')
    for idx, (dr, dc) in enumerate([[0, 1], [0,-1], [1,0], [-1,0]]):
        nr, nc = r+dr, c+dc
        if ((0<=nr<len(board)) and (0<=nc<len(board[0]))) and (nboard[nr][nc] == 1):
            # 지금 A차례
            if step%2 == 0:
                ret = search(nboard, [nr,nc], bloc, step+1)
            else:
                ret = search(nboard, aloc, [nr, nc], step+1)

            # 내가 이기는 경우, 이기니까 min으로
            if ret[0] == False:
                canWin = True
                minTurn = min(minTurn, ret[1])
            else:
                maxTurn = max(maxTurn, ret[1])

    if canWin == True:
        return (canWin, minTurn+1)
    else:
        return (canWin, maxTurn+1)


def solution(board, aloc, bloc):
    answer = search(board, aloc, bloc, 0)
    return answer[1]