heatgo = {1: [(-1, 1), (0, 1), (1, 1)], 2: [(-1, -1), (0, -1), (1, -1)], 3: [(-1, -1), (-1, 0), (-1, 1)],
          4: [(1, -1), (1, 0), (1, 1)]}
cannotgoRIGHT = {(-1, 1): [(0, 0, 0), (-1, 0, 1)], (0, 1): [(0, 0, 1)], (1, 1): [(1, 0, 0), (1, 0, 1)]}  # 오른쪽 기준
cannotgoLEFT = {(-1, -1): [(0, 0, 0), (-1, -1, 1)], (0, -1): [(0, -1, 1)], (1, -1): [(1, 0, 0), (-1, -1, 1)]}  # 왼쪽 기준
cannotgoUP = {(-1, -1): [(0, -1, 0), (0, -1, 1)], (-1, 0): [(0, 0, 0)], (-1, 1): [(0, 1, 0), (0, 0, 1)]}
cannotgoDOWN = {(1, -1): [(1, -1, 0), (0, -1, 1)], (1, 0): [(1, 0, 0)], (1, 1): [(1, 1, 0), (0, 0, 1)]}  # 아래쪽 기준
# 오른쪽 왼쪽 위 아래
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def check_go(row, col, dir):  # 해당 방향으로 이동할 수 있는지 (범위, 벽 체크)
    update = []
    go_cand = heatgo[dir]
    if dir == 1:
        not_cand = cannotgoRIGHT
    elif dir == 2:
        not_cand = cannotgoLEFT
    elif dir == 3:
        not_cand = cannotgoUP
    elif dir == 4:
        not_cand = cannotgoUP

    for i in range(3):
        flag = True
        drow, dcol = row + go_cand[i][0], col + go_cand[i][1]
        for w in not_cand[(go_cand[i][0], go_cand[i][1])]:
            wrow, wcol = row + w[0], col + w[1]
            if (wrow, wcol, w[2]) in wall:
                flag = False
                break
        if flag:
            continue
        else:
            update.append((drow, dcol))

