from collections import deque
def can_move(cur1, cur2, new_board):
    Y, X = 0, 1
    cand = []
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 평행이동
    for dy, dx in DELTAS:
        nxt1 = (cur1[Y]+dy, cur1[X] + dx)
        nxt2 = (cur2[Y]+dy, cur2[X]+dx)
        if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[Y]] == 0:
            cand.append((nxt1, nxt2))
    # 회전
    if cur1[Y] == cur2[Y]: # 가로방향일 때
        UP, DOWN = -1, 1
        for d in [UP, DOWN]:
            if new_board[cur1[Y]+d][cur1[X]] == 0 and new_board[cur1[Y]+d][cur2[X]] == 0:
                cand.append((cur1, (cur1[Y]+d, cur1[X])))
                cand.append((cur2, (cur2[Y]+d, cur2[X])))
    else: # 세로 방향일 때
        LEFT, RIGHT = -1, 1
        for d in [LEFT, RIGHT]:
            if new_board[cur1[Y]][cur1[X]+d] == 0 and new_board[cur2[Y]][cur2[X]+d] == 0:
                cand.append((cur1, (cur1[Y], cur1[X]+d)))
                cand.append((cur2, (cur2[Y], cur2[X]+d)))
    return cand

# 왜 외벽을 확장하는지 (예외처리 하기 귀찮아서)
# 왜 새로운 장소가 둘다 OFF일떄 이동하는지 ( board이기 때문)

def solution(board):
    N = len(board)
    new_board = [[1]*(N+2) for _ in range(N+2)]

    for i in range(N):
        for j in range(N):
            new_board[i+1][j+1] = board[i][j]

    que = deque([((1, 1), (1, 2), 0)])
    confirm = set([((1, 1), (1, 2))])

    while que:
        cur1, cur2, count = que.popleft()
        if cur1 == (N, N) or cur2 == (N, N):
            return count
        for nxt in can_move(cur1, cur2, new_board):
            if nxt not in confirm:
                que.append((*nxt, count+1))
                confirm.add(nxt)