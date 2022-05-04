from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def checkout(row, col):
    if row<0 or row>=5 or col<0 or col>=5:
        return True
    return False

def bfs(row, col, place):
    visited = [[False]*5 for _ in range(5)]
    queue = deque([])
    queue.append((row, col))
    visited[row][col] = True

    while queue:
        nr, nc = queue.popleft()
        for k in range(4):
            # 여기서 네방향만 확인함
            drow, dcol = nr+dx[k], nc+dy[k]
            if checkout(drow, dcol):
                continue
            # 처음 확인하는 사람인 경우
            if not visited[drow][dcol] and abs(drow-row)+abs(dcol-col) <= 2: # 2이하면 파티션이라도 우선 탐색을 먼저 해야됏음 디버깅으로 해결
                visited[drow][dcol] = True
                queue.append((drow, dcol))
                if place[drow][dcol] == 'P':
                    visited[drow][dcol] = True
                    queue.append((drow, dcol))
                    # 거리가 1인 경우
                    if abs(drow-row)+abs(dcol-col) == 1:
                        return False
                    # 거리가 2인 경우
                    else:
                        if drow == row:
                            if place[drow][(dcol+col)//2] == 'O':
                                return False
                        elif dcol == col:
                            if place[(drow+row)//2][dcol] == 'O':
                                return False
                        elif place[drow][col] == 'O' or place[row][dcol] == 'O':
                            return False


    return True

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                if not bfs(i, j, place): # False 나오면 가차X
                    return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer

print(solution(
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
))