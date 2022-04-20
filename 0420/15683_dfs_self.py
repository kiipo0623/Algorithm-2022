import copy

N, M = map(int, input().split())
graph = []
cctv = []
for i in range(N):
    data = list(map(int, input().split()))
    graph.append(data)
    for j in range(M):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j], i, j])

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [3, 1], [1, 2], [2, 0]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

def fill(mode, x, y, temp):
    for m in mode:
        ax = x
        ay = y

        while True:
            nx = ax + dx[m]
            ny = ay + dy[m]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                break
            elif temp[nx][ny] == 6:
                break
            else:
                temp[nx][ny] = 7
                ax, ay = nx, ny
    return temp

def dfs(depth, arr):
    global min_value

    if depth == len(cctv):
        cnt_ = 0
        for i in range(N):
            cnt_ += arr[i].count(0)
        min_value = min(min_value, cnt_)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for i in mode[cctv_num]:
        temp = fill(i, x, y, temp)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)


min_value = int(1e9)
dfs(0, graph)
print(min_value)