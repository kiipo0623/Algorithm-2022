from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    for rec in rectangle:
        rec[0] *= 2
        rec[1] *= 2
        rec[2] *= 2
        rec[3] *= 2

    characterX *= 2
    characterY *= 2

    itemX *= 2
    itemY *= 2

    visited = [[0]*101 for _ in range(101)]
    answer = 202

    # U D R L
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque([(characterX, characterY)])
    visited[characterX][characterY] = 1
    checking_rec = [0 for _ in range(len(rectangle))]

    while q:
        x, y, cnt = q.popleft()
        if (x, y) == (itemX, itemY) and answer > cnt:
            answer = cnt

        for move in moves: # 네 방향 이동에 대해서
            dx, dy = move
            next_x = x + dx
            next_y = y + dy

            if not (1<=next_x<=100 and 1<=next_y<=100): # 좌표 범위를 벗어날 때
                continue
            if visited[next_x][next_x] == 1: # 방문한 적이 있을 때
                continue
            for i, rec in enumerate(rectangle): # 모든 사각형에 대해서
                s_x, s_y, e_x, e_y = rec
                # 1. 사각형을 벗어나는 경우 : 네 개 모두 벗어나지만 않으면 된다
                if (next_x < s_x or next_x > e_x) or (next_y < s_y or next_y > e_y):
                    checking_rec[i] = -1
                    continue
                # 2. 사각형 내부에 해당하는 경우 : 무조건 안된다
                if (s_x<next_x<e_x) and (s_y < next_y < e_y):
                    checking_rec[i] = -2
                    break
                checking_rec[i] = 1 # 정상 이동
            if -2 in checking_rec or 1 not in checking_rec:
                continue
            visited[next_x][next_y] = 1
            q.append((next_x, next_y, cnt+1))
    return answer//2