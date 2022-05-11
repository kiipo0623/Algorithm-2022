dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(board):
    answer = 0
    N = len(board)
    def available(row, col):
        if row<0 or col<0 or row>=N or col>=N:
            return False
        if board[row][col] == 1:
            return False
        return True

    def makeorder(row1, col1, row2, col2):
        if row1 != row2:
            if row1<row2:
                return [(row1, col1), (row2, col2)]
            elif row1>row2:
                return [(row2, col2), (row1, col1)]
        else:
            if col1<col2:
                return [(row1, col1), (row2, col2)]
            else:
                return [(row2, col2), (row1, col1)]

    def bt(visited, cnt, nowpos1, nowpos2):
        nonlocal answer
        if (nowpos1[0] == N-1 and nowpos1[1] == N-1) or (nowpos2[0] == N-1 and nowpos2[1] == N-1):
            answer = min(answer, cnt)

        for k in range(4):
            next_row1, next_col1 = nowpos1[0]+dx[k], nowpos1[1]+dy[k]
            next_row2, next_col2 = nowpos2[0]+dx[k], nowpos2[1]+dy[k]
            if available(next_row1, next_col1) and available(next_row2, next_col2):
                if k<2:
                    if board[next_row1][next_col1]*board[next_row2][next_col2] == 0: # 가로인 경우
                        for idx, val in enumerate(makeorder(next_row1, next_col1, next_row2, next_col2)):
                            visited.append((val[0], val[1], 0, idx))

                else: # 세로인 경우
                    




    return answer