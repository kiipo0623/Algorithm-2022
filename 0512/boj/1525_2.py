import sys
from collections import deque
sys.setrecursionlimit(10**6)

board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ANS = '123456780'
visited = dict()

def bfs(b, nowzero):
    queue = deque([])
    queue.append((nowzero, 0, b))

    while queue:
        zeropos, cnt, bstr = queue.popleft()
        tmpboard = make_board(bstr)
        for k in range(4):
            drow, dcol = zeropos[0]+dx[k], zeropos[1]+dy[k]
            if not checkout(drow, dcol):
                tb = [a[:] for a in tmpboard]
                tb[drow][dcol], tb[zeropos[0]][zeropos[1]] = tb[zeropos[0]][zeropos[1]], tb[drow][dcol]
                sol = visited.get(make_str(tb))
                if sol is None or sol >= cnt+1:
                    visited[make_str(tb)] = cnt+1
                    queue.append(([drow, dcol], cnt+1, make_str(tb)))


def checkout(row, col):
    if row<0 or col<0 or row>=3 or col>=3:
        return True
    return False

def make_str(b):
    res = ''
    for i in range(3):
        res += ''.join(b[i])
    return res

def make_board(s):
    b = []
    for i in range(0, 9, 3):
        b.append(list(s[i:i+3]))
    return b

start = [-1, -1]
for i in range(3):
    data = list(input().split())
    for j in range(3):
        if data[j] == '0':
            start = [i, j]
    board.append(data)


default = make_str(board)
if default == ANS:
    print(0)
    exit()
else:
    bfs(default, start)

if visited.get(ANS):
    print(visited.get(ANS))
else:
    print(-1)