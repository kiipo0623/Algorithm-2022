def check(x, y, d1, d2):
    global N
    if not x<x+d1+d2<N:
        return False
    if y-d1 <= 1 or y+d2 >= N:
        return False
    return True

def simulation(x, y, d1, d2):
    global N, board
    filter = [[False]*N for _ in range(N)]
    # 5번 선거구 제거
    print(x, y, d1, d2)
    for i in range(d1+1): # 0 1 2 3 ... d1
        filter[y-i][x+i] = True
        filter[y+d2-i][x+d2+i] = True
    for i in range(d2+1):
        filter[y+i][x+i] = True
        filter[y-d1+i][x+d1+i] = True

    # 1-4번 선거구 제거
    people = [0]*6
    for col in range(x, y-d1+d2+1):
        flag = False
        for row in range(N):
            if flag:
                people[5] += board[row][col]
            if not flag and filter[row][col]:
                flag = True
                people[5] += board[row][col]
            elif flag and filter[row][col]:
                flag = False
    print(people[5])


N = int(input())
board = []
answer = int(1e9)

for _ in range(N):
    board.append(list(map(int, input().split())))

for x in range(0, N):
    for y in range(1, N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if check(x, y, d1, d2):
                    simulation(x,y , d1, d2)