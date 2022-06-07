dir = ((-1, 0), (0, 1), (1, 0), (0, -1))

# cnt : 게잉 이동 횟수
# flag의 의미가 뭔
# A > B > A > B > A 이런식으로 쭉 호출하니까 마지막에 A가 리턴하게 됨
def A_turn(ar, ac, br, bc, cnt, board):
    if board[ar][ac] == 0: # 자기가 지는경우 (상대에게 1 리턴하니까)
        return (1, cnt) # (내가 진다, 이동 횟수)

    winner = [] # 승리 시 이동 횟수 저장
    loser = [] # 패배 시 이동 횟수 저장
    flag = False # 이동 여부 ( 이동할 수 없으면 필패 )

    for dr, dc in dir:
        nr, nc = ar+dr, ac+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1: # 한번이라도 이동했을 때 flag = True
            flag = True
            temp = [row[:] for row in board]
            temp[ar][ac] = 0
            iswin, turn = B_turn(br, bc, nr, nc, cnt+1, temp) # 이동 상태 변화 후 재귀 호출

            # 결과를 받았을 때 승리/패배에 따라 후처리
            if iswin:
                winner.append(turn) # turn : cnt
            else:
                loser.append(turn)

    # 네 방향에 대해 모든 경우의 수 완료했을 때
    if flag:
        # 한 텀 안에서 승리 패배 모두 할 수 있지만 둘 다 이기는 경우만 고려
        if winner: # (승리)
            return (0, min(winner))
        else: # (패배)
            return (1, max(loser))
    # 이동 못하면 질 수밖에 없다
    else: # (패배)
        return (1, cnt)

def B_turn(br, bc, ar, ac, cnt, board):
    if board[br][bc] == 0:
        return (1, cnt)

    winner = []
    loser = []
    flag = False

    for dr, dc in dir:
        nr, nc = br+dr, bc+dc
        if 0<= nr < len(board) and 0<=nc<len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [row[:] for row in board]
            temp[br][bc] = 0
            iswin, turn = A_turn(ar, ac, nr, nc, cnt+1, temp)

            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)

    if flag:
        if winner:
            return (0, min(winner))
        else:
            return (1, max(loser))
    else:
        return (1, cnt)

def solution(board, aloc, bloc):
    ar, ac, br, bc = aloc[0], aloc[1], bloc[0], bloc[1]
    # A부터 하기 때문에
    answer = A_turn(ar, ac, br, bc, 0, board)[1]
    return answer

print(solution(
[[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1,0], [1,2]
))