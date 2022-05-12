dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [[0]*(51) for _ in range(51)]

def checkout(row, col):
    if row<0 or col<0 or row>=51 or col>=51:
        return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    global board
    answer = 0
    # x : col y : row
    for rec in rectangle:
        LDx, LDy, RUx, RUy = rec
        low, high, left, right = abs(50-LDy), abs(50-RUy), abs(LDx), abs(RUx)
        side_row = [low, high]
        side_col = [left, right]

        for i in range(high, low+1):
            for j in range(left, right+1):
                if board[i][j] == 0:
                    if i in side_row or j in side_col:
                        board[i][j] = 1
                    else:
                        board[i][j] = -1

                elif board[i][j] == 1:
                    if i in side_row or j in side_col:
                        board[i][j] = 1
                    else:
                        board[i][j] = -1

    mv_dir = []
    # mv_start = []
    r_pos, c_pos = abs(characterY-50), abs(characterX)
    for k in range(4):
        if board[r_pos+dx[k]][c_pos+dy[k]] == 1:
            mv_dir.append(k)
            # mv_start.append((r_pos+dx[k], c_pos+dy[k]))

    # X_pos, Y_pos = abs(itemX), abs(itemY-50)
    print(board)
    print(mv_dir)
    return answer

# print(solution(
# [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8
# ))

print(solution(
[[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3
))