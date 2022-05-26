N = int(input())
board = []
answer = int(1e9)

for _ in range(N):
    board.append(list(map(int, input().split())))


def check(x, y, d1, d2):
    global N
    if x+d1+d2 >= N:
        return False
    if y-d1 < 0 or y + d2 >=N:
        return False
    return True

def simulate(x, y, d1, d2):
    global N, board
    b = [a[:] for a in board]
    # 필터 설정
    filter = [[False]*N for _ in range(N)]
    for i in range(d1+1):
        filter[y-i][x+i] = True
        filter[y+d2-i][x+d2+i] = True
    for i in range(d2+1):
        filter[y+i][x+i] = True
        filter[y-d1+i][x+d1+i] = True
    print(filter)

    people = [0]*6
    # 5번 선거구 확정
    for col in range(x, x+d1+d2+1):
        flag = False
        for row in range(N):
            if not flag and filter[row][col]:
                flag = True
                people[5] += b[row][col]
                b[row][col] = 0
            elif flag and not filter[row][col]:
                break
            elif flag:
                people[5] += b[row][col]
                b[row][col] = 0
    # 1~4선거구
    for row in range(y+1):
        for col in range(x+d1):
            people[1] += b[row][col]

    for row in range(y+1, N):
        for col in range(x+d2+1):
            people[2] += b[row][col]

    for row in range(y - d1 + d2):
        for col in range(x+d1, N):
            people[3] += b[row][col]

    for row in range(y -d1+d2, N):
        for col in range(x+d2+1, N):
            people[4] += b[row][col]

    print("x ", x, "y ", y, "d1 ", d1, "d2 ", d2)
    print(people)
    return max(people[1:]) - min(people[1:])

def select():
    global answer
    for x in range(0, N):
        for y in range(1, N):
            for d1 in range(1, N):
                for d2 in range(1, N):
                    if check(x, y, d1, d2):
                        answer = min(answer, simulate(x, y, d1, d2))


select()
print(answer)