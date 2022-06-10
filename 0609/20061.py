# x = row
# y = col
def put_blue(t, x, y):
    global blue
    if t == 1:
        for i in range(7):
            if blue[x][i] == 1:
                blue[x][i-1] = 1
                return

    elif t == 2:
        for i in range(6):
            if blue[x][i+1] == 1:
                blue[x][i-1] = 1
                blue[x][i] = 1
                return

    elif t == 3:
        for i in range(7):
            if blue[x][i] == 1 or blue[x+1][i] == 1:
                blue[x][i-1] = 1
                blue[x+1][i-1] = 1
                return

def put_green(t, x, y):
    global green
    if t == 1:
        for i in range(7):
            if green[i][y] == 1:
                green[i-1][y] = 1
                return
    elif t == 2:
        for i in range(7):
            if green[i][y] == 1 or green[i][y+1] == 1:
                green[i-1][y] = 1
                green[i-1][y+1] = 1
                return
    elif t == 3:
        for i in range(6):
            if green[i+1][y] == 1:
                green[i-1][y] = 1
                green[i][y] = 1
                return

def get_grade_blue():
    global blue, answer
    update = []
    for i in range(5, -1, -1):
        flag = True
        for j in range(4):
            if blue[j][i] != 1:
                flag = False
                break
        if flag:
            update.append(i)

    answer += len(update)
    for idx, line in enumerate(update):
        for i in range(4):
            blue[i][line+idx] = 0

        for i in range(line+idx, 0, 1):
            blue[0][i], blue[1][i], blue[2][i], blue[3][i] = blue[0][i-1], blue[1][i-1], blue[2][i-1], blue[3][i-1]

        for i in range(4):
            blue[i][0] = 0

def get_grade_blue_re():
    global blue, answer
    while True:
        flag = False
        line = -1
        for i in range(5, -1, -1):
            if blue[0][i] == blue[1][i] == blue[2][i] == blue[3][i] == 1:
                flag = True
                answer += 1
                line = i
                break

        if not flag:
            break
        for i in range(line, 0, -1):
            blue[0][i], blue[1][i], blue[2][i], blue[3][i] = blue[0][i-1], blue[1][i-1], blue[2][i-1], blue[3][i-1]
        for i in range(4):
            blue[0][i] = 0

def get_grade_green_re():
    global green, answer
    while True:
        flag = False
        line = -1
        for i in range(5, -1, -1):
            if green[i][0] == green[i][1] == green[i][2] == green[i][3] == 1:
                flag = True
                answer += 1
                line = i
                break

        if not flag:
            break
        for i in range(line, 0, -1):
            green[i][0], green[i][1], green[i][2], green[i][3] = green[i-1][0], green[i-1][1], green[i-1][2], green[i-1][3]
        for i in range(4):
            green[0][i] = 0


def get_grade_green():
    global green, answer
    update = []
    for i in range(5, -1, -1):
        flag = True
        for j in range(4):
            if green[i][j] != 1:
                flag = False
                break
        if flag:
            update.append(i)

    answer += len(update)
    for idx, line in enumerate(update):
        for i in range(4):
            green[line+idx][i] = 0

        for i in range(line+idx, 0, -1):
            green[i][0], green[i][1], green[i][2], green[i][3] = green[i-1][0], green[i-1][1], green[i-1][2], green[i-1][3]

        for i in range(4):
            green[0][i] = 0



def remove_blue():
    global blue
    update = []
    for i in [1, 0]:
        flag = False
        for j in range(4):
            if blue[j][i]:
                flag = True
                break
        if flag:
            update.append(i)

    if len(update) == 0:
        return

    for line in range(5-len(update), len(update)-1, -1):
        blue[0][line+len(update)], blue[1][line+len(update)], blue[2][line+len(update)], blue[3][line+len(update)] = blue[0][line], blue[1][line], blue[2][line], blue[3][line]

    for i in range(4):
        for u in update:
            blue[i][u] = 0


def remove_green():
    global green
    update = []
    for i in [1, 0]:
        flag = False
        for j in range(4):
            if green[i][j]:
                flag = True
                break
        if flag:
            update.append(i)

    if len(update) == 0:
        return

    for line in range(5 - len(update), len(update)-1, -1):
        green[line + len(update)][0], green[line + len(update)][1], green[line + len(update)][2], green[line + len(update)][3] = green[line][0],green[line][1], green[line][2], green[line][3]
    for i in range(4):
        green[0][i] = 0

N = int(input())

blue = [[0 for _ in range(7)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(7)]

for i in range(4):
    blue[i][6] = 1
    green[6][i] = 1
answer = 0

for _ in range(N):
    t, x, y = map(int, input().split())
    print(t, x, y)
    print("blue")
    put_blue(t, x, y)
    print("put blue")
    print(blue)
    get_grade_blue_re()
    print("get grade")
    print(blue)
    remove_blue()
    print("remove")
    print(blue)
    print()

    print("green")
    put_green(t, x, y)
    print("put green")
    print(green)
    get_grade_green_re()
    print("get grade")
    print(green)
    remove_green()
    print("remove")
    print(green)
    print()

print(answer)
cnt = 0
for i in range(6):
    for j in range(4):
        cnt += blue[j][i]
        cnt += green[i][j]
print(cnt)

