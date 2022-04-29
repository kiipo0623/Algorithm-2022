from collections import deque
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def make_turn(N):
    move_cnt = []
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    for i in range(1, N + 1):
        move_cnt.extend([i, i])
    move_queue = []
    row, col = N // 2, N // 2
    cnt = 0
    while not checkout(row, col):
        direct = cnt % 4
        iter = move_cnt[cnt]
        for _ in range(iter):
            drow, dcol = row + dx[direct], col + dy[direct]
            move_queue.append((drow, dcol))
            row, col = drow, dcol
        cnt += 1
    return move_queue[:-1]

def destroy_shark(dir, speed):
    global board
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    shark_row, shark_col = N//2, N//2
    for s in range(1, speed+1):
        drow, dcol = shark_row+dx[dir]*s, shark_col+dy[dir]*s
        board[drow][dcol] = 0

def get_line():
    ball = []
    for row, col in turn_queue:
        ball.append(board[row][col])
    return ball

def boom(line):
    global grade
    stop = False
    while not stop:
        stop = True
        leng = len(line)

        for i in range(leng-1):
            if line[i] == 0:
                continue

            if line[i] == line[i+1]:
                start, end, num, cnt = i, i+1, line[i], 1

                for j in range(i+1, leng):
                    if line[j] == num:
                        end = j
                        cnt += 1
                    else:
                        break

                if cnt>=4:
                    for idx in range(start, end+1):
                        line[idx] = 0
                    grade[num] += cnt
                    stop = False

        while 0 in line:
            line.remove(0)
    return line

def separate(line):
    line = deque(line)
    newline = []
    cnt = 1

    if len(line) == 0:
        return []

    number = line.popleft()
    while line:
        now = line.popleft()
        if number == now: # 이전이랑 같으면
            cnt += 1
        else: # 이전이랑 다르면
            newline.append(cnt)
            newline.append(number)
            number = now
            cnt = 1
    newline.append(cnt)
    newline.append(number)

    return newline

def updateboard(line, turn):
    leng_line, leng_turn = len(line), len(turn)
    if leng_line > leng_turn:
        line = line[:leng_turn]
    else:
        line.extend([0]*(leng_turn-leng_line))

    board = [[0]*N for _ in range(N)]
    for i in range(leng_turn):
        r, c = turn[i]
        board[r][c] = line[i]
    return board

def simulate():
    global board
    for d, s in todo:
        destroy_shark(d, s)
        # print("after destroyshark")
        # print(board)
        line = get_line() # 매 턴마다 한번만 하면 된다
        # print("after getline")
        # print(line)
        # 빈 칸 있으면 하나씩 당겨온다
        while 0 in line:
            line.remove(0)
        # 폭발 진행
        line = boom(line)
        # print("afterboom")
        # print(line)
        # 두개로 분리하기
        newline = separate(line)
        # print("afterseparate")
        # print(newline)
        # 라인에 있는 것 보드 갱신하기
        board = updateboard(newline, turn_queue)
        # print("afterupdateboard")
        # print(board)
        # print()

N, M = map(int, input().split())
grade = {1:0, 2:0, 3:0}
answer = 0
board = []
todo = []
for _ in range(N):
    board.append(list(map(int, input().split())))
for _ in range(M):
    d, s = map(int, input().split())
    todo.append((d, s))
# 순서 구현은 딱 한번만 하면 된다
turn_queue = make_turn(N)
# print("turn", turn_queue)
simulate()
for g in grade:
    answer += g*grade[g]
print(answer)