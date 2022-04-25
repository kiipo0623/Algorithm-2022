# 청소년 상어
import copy
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
arr = []
fish = [[0]]
for k in range(4):
    temp = list(map(int, input().split()))
    arr.append([temp[i] for i in range(0, len(temp), 2)])
    for i in range(0, len(temp), 2):
        fish.append([temp[i], [k, i//2, temp[i+1]]])


def fish_move(arr, fish):
    for i, temp in enumerate(fish):
        if i != 0:
            x, info = temp
            if not eat[x]:
                x, y, dir = info
                while True:
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] != 'shark':
                        if arr[nx][ny] == 0:
                            temp = arr[x][y]
                            fish[temp][1][0], fish[temp][1][1] = nx, ny
                            arr[nx][ny] = arr[x][y]
                            arr[x][y] = 0
                        else:
                            change_fish(arr, fish, x, y, nx, ny)
                        break
                    else:
                        dir = change_dir(dir)
                        fish[i][1][2] = dir


def change_fish(arr, fish, x, y, nx, ny):
    fish[arr[x][y]][1][0] = nx
    fish[arr[x][y]][1][1] = ny
    fish[arr[nx][ny]][1][0] = x
    fish[arr[nx][ny]][1][1] = y
    temp = arr[x][y]
    arr[x][y] = arr[nx][ny]
    arr[nx][ny] = temp


def change_dir(dir):
    ndir = dir + 1
    if ndir == 9:
        ndir = 1
    return ndir


def shark_eat_dfs(arr, fish, now, cnt):
    global result
    temp = copy.deepcopy(arr)
    fish_temp = copy.deepcopy(fish)
    fish_move(temp, fish_temp)
    can_eat_list = shark_can_eat(temp, fish_temp, now)
    for x in can_eat_list:
        if temp[x[0]][x[1]] != 0:
            t = temp[x[0]][x[1]]
            eat[temp[x[0]][x[1]]] = True
            temp[x[0]][x[1]] = 'shark'
            temp[now[0]][now[1]] = 0
            shark_eat_dfs(temp, fish_temp, x, cnt+t)
            temp[x[0]][x[1]] = t
            temp[now[0]][now[1]] = 'shark'
            eat[temp[x[0]][x[1]]] = False
    result = max(result, cnt)


def shark_can_eat(arr, fish, t):
    temp = []
    x, y, dir = t[0], t[1], t[2]
    nx, ny = x+dx[dir], y+dy[dir]
    while 0 <= nx < 4 and 0 <= ny < 4:
        if arr[nx][ny] != 0:
            temp.append(fish[arr[nx][ny]][1])
        nx += dx[dir]
        ny += dy[dir]
    return temp


fish.sort()
eat = [False] * 17
eating = arr[0][0]
arr[0][0] = 'shark'
eat[eating] = True

result = 0
shark_eat_dfs(arr, fish, fish[eating][1], fish[eating][0])
print(result)