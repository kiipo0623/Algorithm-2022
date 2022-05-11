def solution(n, build_frame):
    answer = []
    board = [[-1]*(n+1) for _ in range(n+1)]

    for build in build_frame:
        col, row, a, b = build
        if b == 0: # 삭제
            if a == 0: # 기둥
                if board[row+1][col] == 0: # 위에 다른 기둥
                    continue
                if board[row+1][col] == 1 and board[row][col+1] != 0: # 위에 다른 보 / 다른 기둥 없음
                    continue
                if board[row+1][col-1] == 1 and board[row][col-1] != 0: # 위에 다른 보 / 다른 기둥 없음
                    continue
                if board[row+1][col] == 1 and (board[row+1][col-1] != 1 and board[row+1][col+1] != 1):
                    continue
                if board[row+1][col-1] == 1 and (board[row+1][col-2] != 1 and board[row+1][col] != 1):
                    continue
                board[row][col] = -1
            elif a == 1: #
                # 보의 한쪽 끝에 기둥이 있는 경우 : 다른 보가 없고/아래 기둥이 없으면
                if board[row][col+1] == 0:
                    continue
                # 양쪽 끝부분 다른 보
                elif board[row][col+1] == 1 and board[row-1][col+1] != 0 and board[row-1][col+2] != 0:
                    continue
                elif board[row][col-1] == 1 and board[row-1][col-1] != 0 and board[row-1][col] != 0:
                    continue
                board[row][col] = -1

        elif b == 1: # 설치
            if a == 0: # 기둥
                if row == 0:
                    board[row][col] = 0
                elif board[row][col-1] == 1:
                    board[row][col] = 0
                elif board[row-1][col] == 0:
                    board[row][col] = 0
            elif a == 1:
                if board[row-1][col] == 0 or board[row-1][col+1] == 0:
                    board[row][col] = 1
                elif board[row][col-1] == 1 and board[row][col+1] == 1:
                    board[row][col] = 1

    for i in range(n+1):
        for j in range(n+1):
            if board[i][j] != -1:
                answer.append([j, i, board[i][j]])
    answer.sort(key=lambda x : (x[0], x[1], x[2]))
    return answer

print(solution(
5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
))
print(solution(
5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
))