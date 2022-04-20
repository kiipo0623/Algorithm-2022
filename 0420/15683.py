from copy import deepcopy
def find_cctv():
    pos = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and graph[i][j] != 6:
                pos.append([graph[i][j], i, j])
    return pos

def simulation(dir_list, row, col):
    def simul_up(row, col):
    # up
        for i in range(row, -1, -1):
            if graph[i][col] == 6:
                break
            else:
                graph[i][col] = 7

    def simul_down(row, col):
        for i in range(row, N):
            if graph[i][col] == 6:
                break
            else:
                graph[i][col] = 7

    def simul_left(row, col):
        for i in range(col, -1, -1):
            if graph[row][i] == 6:
                break
            else:
                graph[row][i] = 7

    def simul_right(row, col):
        for i in range(col, N):
            if graph[row][i] == 6:
                break
            else:
                graph[row][i] = 7

def countgraph(cctv, row, col):
    def count_up(row, col):
        cnt = 0
        # up
        for i in range(row, -1, -1):
            if graph[i][col] == 6:
                break
            elif graph[i][col] == 0:
                cnt += 1
        return cnt

    def count_down(row, col):
        cnt = 0
        for i in range(row, N):
            if graph[i][col] == 6:
                break
            elif graph[i][col] == 0:
                cnt += 1

    def count_left(row, col):
        cnt = 0
        for i in range(col, -1, -1):
            if graph[row][i] == 6:
                break
            elif graph[row][i] == 0:
                cnt += 1

    def count_right(row, col):
        cnt = 0
        for i in range(col, N):
            if graph[row][i] == 6:
                break
            elif graph[row][i] == 0:
                cnt += 1

    if cctv == 1:
        # 상 하 좌 우
        testlist = []
        testlist.append(count_up(row, col))
        testlist.append(count_down(row, col))
        testlist.append(count_left(row, col))
        testlist.append(count_right(row, col))
        return [testlist.index(max(testlist))]

    elif cctv == 2:
        ud = count_up(row, col) + count_down(row, col)
        lr = count_left(row, col) + count_down(row, col)
        if ud>=lr:
            return [1,2]
        else:
            return [3,4]



N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

cctv_position = find_cctv()
for cctv in cctv_position:
