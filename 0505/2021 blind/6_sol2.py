from collections import defaultdict, deque
from itertools import permutations
direct = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def checkout(row, col):
    if row<0 or col<0 or row>=4 or col>=4:
        return True
    return False

def move_cost(board, start, end): # 조작 횟수 카운트. board 사용 대신 cnt값을 넘김
    if start == end:
        return 0
    queue, visit = deque([start[0], start[1], 0]), {start}
    while queue:
        x, y, c = queue.popleft()
        for dx, dy in direct:
            nx, ny = x + dx, y + dy # 일반 이동
            cx, cy = x, y # ctrl 이동
            while True:
                cx, cy = cx+dx, cy+dy
                if checkout(cx, cy):
                    cx, cy = cx-dx, cy-dy # 원상복구
                    break
                elif board[cx][cy] != 0: # 뭔가 있으면
                    break

        if (nx, ny) == end or (cx, cy) == end:
            return c+1
        if not checkout(nx, ny) and (nx,ny) not in visit:
            queue.append((nx, ny, c+1))
            visit.add((nx, ny))
        if (cx, cy) not in visit:
            queue.append((cx, cy, c+1))
            visit.add((cx, cy))


def cls_cost(board, cdict, cur, order, cost):
    if len(order) == 0:
        return cost # 모든 카드를 확인한 경우
    idx = order[0]+1

    choice1 = move_cost(board, cur, cdict[idx][0]) + move_cost(board, cdict[idx][0], cdict[idx][1]) + 2
    choice2 = move_cost(board, cur, cdict[idx][1]) + move_cost(board, cdict[idx][1], cdict[idx][0]) + 2

    # 선택한 카드는 board에서 0으로 변경
    new_board = [a[:] for a in board]
    new_board[cdict[idx][0][0]][cdict[idx][0][1]] = 0
    new_board[cdict[idx][1][0]][cdict[idx][1][1]] = 0

    if choice1 < choice2:
        return cls_cost(new_board, cdict, cdict[idx][1], order[1:], cost + choice1)
    else:
        return cls_cost(new_board, cdict, cdict[idx][0], order[1:], cost + choice2)

def solution(board, r, c):
    answer = int(1e9)
    cdict = defaultdict(list)


    for row in range(4):
        for col in range(4):
            if board[row][col]:
                cdict[board[row][col]].append((row, col))

    for case in permutations(list(cdict.keys()), len(cdict)):
        answer = min(answer, cls_cost(board, cdict, (r, c), case, 0))
