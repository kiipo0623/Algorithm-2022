dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]
# 사전순 비교 매번 하면 됨 (변수 필요 없음)
# 몇마리 죽일 수 있는지 카운트

def checkout(row, col):
    if row<0 or row>=4 or col<0 or col>=4:
        return True
    return False

# 죽인거개수, 루트
# 현재위치 지금까지방향 죽인거 개수 보드
# fishboard = 개수
def shark_bt(r, c, dir, kill, fishboard):
    global shark_route_cand
    if len(dir) == 3:
        s = ''
        for i in range(3):
            s += str(dir[i])
        shark_route_cand.append((kill, s))
        return

    for k in range(1, 5):
        drow, dcol = r+dx[k], c+dy[k]
        if not checkout(drow, dcol):
            eatfish = fishboard[drow][dcol]
            dir.append(k)
            fishboard[drow][dcol] = 0
            shark_bt(drow, dcol, dir, kill+eatfish, fishboard)
            dir.pop()
            fishboard[drow][dcol] = eatfish

shark_route_cand = []
fishboard = [[0, 0, 1, 1], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 1]]
shark_bt(3, 1, [], 0, fishboard)
shark_route_cand.sort(key = lambda x:(-x[0], x[1]))
print(shark_route_cand)
print(len(shark_route_cand))