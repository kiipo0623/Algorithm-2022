from collections import defaultdict, deque
from copy import deepcopy
from math import floor
direction = {0: [-1, 0], 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[1, 0], 5:[1, -1], 6:[0, -1], 7:[-1, -1]}

def new_rc(row, col,speed, dir):
    for s in range(speed):
        drow, dcol = row + direction[dir][0], col + direction[dir][1]
        if drow==-1:
            drow = N-1
        elif drow==N:
            drow = 0
        if dcol==-1:
            dcol = N-1
        elif dcol == N:
            dcol = 0
        row, col = drow, dcol
    return row, col

def move_ball():
    new_fireball = defaultdict(deque)
    new_ballqueue = deque()
    while ballqueue:
        row, col = ballqueue.popleft()
        while fireball[(row, col)]:
            m, s, d = fireball[(row, col)].popleft()
            n_row, n_col = new_rc(row, col, s, d)

            if len(new_fireball[(n_row, n_col)]) == 0:
                new_ballqueue.append((n_row, n_col))
            elif len(new_fireball[(n_row, n_col)]) == 1:
                multiqueue.append((n_row, n_col))

            new_fireball[(n_row, n_col)].append((m, s, d))
    return new_fireball, new_ballqueue

def remove_ball(new_fireball):
    while multiqueue:
        row, col = multiqueue.popleft()
        m_update, s_update, d_update, cnt = 0, 0, set(), 0

        while new_fireball[(row, col)]:
            m, s, d = new_fireball[(row, col)].popleft()
            m_update += m
            s_update += s
            d_update.add(d%2)
            cnt += 1
        m_update = floor(m_update/5)
        s_update = floor(s_update/cnt)

        if len(d_update) == 1:
            d_update = (0, 2, 4, 6)
        else:
            d_update = (1, 3, 5, 7)

        if m_update == 0: # 질량이 0이면 소멸된다
            del new_fireball[(row, col)]
            ballqueue.remove((row, col))
        else:
            for nd in d_update:
                new_fireball[(row, col)].append((m_update, s_update, nd))
    return new_fireball

def simulate():
    global ballqueue, fireball, multiqueue
    for i in range(K):
        new_fb, new_bq = move_ball()
        ballqueue = deepcopy(new_bq)
        rmv_fb = remove_ball(new_fb)
        fireball = deepcopy(rmv_fb)

N, M, K = map(int, input().split())
fireball = defaultdict(deque)
ballqueue = deque()
multiqueue = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r-1, c-1
    fireball[(r, c)].append([m, s, d])
    ballqueue.append((r, c))
simulate()
answer = 0
while ballqueue:
    row, col = ballqueue.popleft()
    while fireball[(row, col)]:
        m, _, _ = fireball[(row, col)].popleft()
        answer += m
print(answer)