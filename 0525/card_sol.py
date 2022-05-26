from itertools import permutations
from collections import deque
def ctrl(board, x0, y0, dx, dy):
    for i in range(1, 4):
        if 0<=(x1:=x0+dx*i)<4 and 0<=(y1:=y0+dy*i)<4:
            if board[x1][y1] > 0: # 값 있으면 종료
                return (x1, y1)
            l = i
    return (x0+dx*l, y0+dy*l) # 값 없으면 최대 이동가능한 곳까지 이동

# xy0 : 출발지 xy1 : 도착지
def move(board, xy0, xy1):
    dist = [[6]*4 for _ in range(4)] # 6:최대 default값
    q = deque([(xy0, 0)]) # 좌표, 비용
    while q:
        [x, y], d = q.popleft()
        if d < dist[x][y]: # 더 가까울때만 진행
            dist[x][y] = d
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0<=x+dx<4 and 0<=y+dy<4:
                    q.append(((x+dx, y+dy), d+1))
                    q.append(((ctrl(board, x, y, dx, dy), d+1)))
    return dist[xy1[0]][xy1[1]]


def solution(board, r, c):
    loc =  {k:[] for k in range(1, 7)} # defaultdict 사용안해도 된다
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                loc[board[i][j]].append((i, j))

    minv = 100

    for p in permutations(filter(lambda v: v, loc.values())):
        sumv = 0 # 해당 순서로 탐색하는데 걸리는 시간
        xys = [(r, c)] # 시작점
        stage = [[v for v in w] for w in board]
        for xy1, xy2 in p: # 두개 같은 카드 중에서 뭐먼저 할지
            vs = [(move(stage, xy, xy1) + move(stage, xy1, xy2), xy2) for xy in xys]\
                 + [(move(stage, xy, xy2) + move(stage, xy2, xy1), xy1) for xy in xys]

            stage[xy1[0]][xy1[1]] = stage[xy2[0]][xy2[1]] = 0
            sumv += 2 + (mvn := min(vs)[0])
            xys = [xy for m, xy in vs if m == mvn]
        minv = min(sumv, minv)
    return minv

print(solution(
[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0
))
