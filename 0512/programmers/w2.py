dot = set()
INF = float('inf')
MIN_ROW, MIN_COL = INF, INF
MAX_ROW, MAX_COL = -INF, -INF
# 전부 x,y /// COL, ROW 형태
def check(lst1, lst2):
    global MIN_ROW, MIN_COL, MAX_ROW, MAX_COL
    A, B, E = lst1
    C, D, F = lst2

    if A*D - B*C == 0:
        return
    else:
        x = (B*F - E*D)/(A*D-B*C)
        y = (E*C - A*F)/(A*D-B*C)

        if x - int(x) == 0 and y - int(y) == 0:
            x = int(x)
            y = int(y)

            if x<MIN_COL: MIN_COL = x
            if x>MAX_COL: MAX_COL = x
            if y<MIN_ROW: MIN_ROW = y
            if y>MAX_ROW: MAX_ROW = y

            dot.add((x, y))
        return


def solution(line):
    global dot, MIN_ROW, MAX_ROW, MIN_COL, MAX_COL
    #좌표 계산
    for l1 in range(len(line)):
        for l2 in range(l1+1, len(line)):
            check(line[l1], line[l2])

    board = [['.']*(MAX_COL-MIN_COL+1) for _ in range(MAX_ROW-MIN_ROW+1)]

    for x, y in dot:
        # print(y, x)
        # print(abs(MAX_ROW - y), abs(MIN_COL - x))
        board[abs(MAX_ROW - y)][abs(MIN_COL - x)] = '*'

    ans = []
    for b in board:
        ans.append(''.join(b))

    return ans




print(solution(
[[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
))