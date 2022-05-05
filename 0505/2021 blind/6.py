from collections import defaultdict
# 상 하 좌 우
direct  = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def use_ctrl(sr, sc, dir, board):
    while True:
        sr += direct[dir][0]
        sc += direct[dir][1]
        if dir == 0 and (sr == 0 or board[sr][sc]!=0):
            return [sr, sc]
        elif dir == 1 and (sr == 3 or board[sr][sc]!=0):
            return [sr, sc]
        elif dir == 2 and (sc == 0 or board[sr][sc]!=0):
            return [sr, sc]
        elif dir == 3 and (sc == 3 or board[sr][sc]!=0):
            return [sr, sc]

def simul(sr, sc, pos_order):
    sum_move = 0
    for i in range(len(pos_order)):
        dr, dc = pos_order[i][0], pos_order[i][1]
        # row이동 후 col이동
        rcmove = 0
        if sr != dr:
            d = 0 if sr < dr else d = 1
            ctrl_row, ctrl_col = use_ctrl(sr, sc, d)
            rcmove += min(abs(sr, dr), abs(ctrl_row - sr) + 1)
            sr = dr
        if sc != dc:
            d = 2 if sc < dc else d = 3
            ctrl_row, ctrl_col = use_ctrl(sr, sc, d)
            rcmove += min(abs(sc, dc), abs(ctrl_col - dc) + 1)
        # col이동 후 row이동


def bt(cnt, fin, pos_order, num_visit):
    global answer, pos_dict, card_list
    if cnt == fin:
        print(pos_order)
        # answer = min(simul(pos_order), answer)

    # 사용하지 않은 num에 대해서 두 좌표 순서 다르게해서 추가
    for i in card_list:
        if i not in num_visit:
            # 순서 첫번째
            tmp1 = pos_order[:]
            tmp1.append(pos_dict[i][0])
            tmp1.append(pos_dict[i][1])
            num_visit.append(i)
            bt(cnt+1, fin, tmp1, num_visit)
            tmp1.pop()
            tmp1.pop()
            num_visit.pop()

            # 순서 두번쨰
            tmp2 = pos_order[:]
            tmp2.append(pos_dict[i][1])
            tmp2.append(pos_dict[i][0])
            num_visit.append(i)
            bt(cnt+1, fin, tmp2, num_visit)
            tmp2.pop()
            tmp2.pop()
            num_visit.pop()


def solution(board, r, c):
    global answer, pos_dict, card_list
    answer = int(1e9)
    pos_dict = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                pos_dict[board[i][j]].append((i, j))

    card_list = list(sorted(list(pos_dict.keys())))
    bt(0, len(card_list), [], [])

    return answer

print(solution(
[[1,0,0,4],[2,0,0,0],[0,0,0,2],[4,0,1,0]], 1, 3
))