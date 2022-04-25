from collections import deque
def rotate(qidx, direct, replay):
    global plate
    queue = plate[qidx]
    queue.popleft()
    for r in range(replay):
        if direct == 0:
            tmp = queue.pop()
            queue.appendleft(tmp)
        else:
            tmp = queue.popleft()
            queue.append(tmp)
    queue.appendleft(1001)
    plate[qidx] = queue

def checkupdate():
    flag = False
    global plate
    update_idx_set = set()
    sum_, cnt_ = 0, 0
    for i in range(1, N+1): # 원판
        for j in range(1, M+1): # 원판 내부
            center = plate[i][j]
            if center>0:
                sum_ += center
                cnt_ += 1

            # 왼 오 위 아래
            check = [1001, 1001, 1001, 1001]
            pos = [(-1, -1), (-1, -1), (-1, -1), (-1, -1)]
            if j == 1:
                check[0], check[1] = plate[i][M], plate[i][2]
                pos[0], pos[1] = (i, M), (i, 2)
            elif j == M:
                check[0], check[1] = plate[i][M-1], plate[i][1]
                pos[0], pos[1] = (i, M-1), (i, 1)
            else:
                check[0], check[1] = plate[i][j-1], plate[i][j+1]
                pos[0], pos[1] = (i, j-1), (i, j+1)

            if i == 1:
                check[2], check[3] = plate[2][j], 1001
                pos[2], pos[3] = (2, j), (-1, -1)
            elif i == N:
                check[2], check[3] = 1001, plate[N-1][j]
                pos[2], pos[3] = (-1, -1), (N-1, j)
            else:
                check[2], check[3] = plate[i+1][j], plate[i-1][j]
                pos[2], pos[3] = (i+1, j), (i-1, j)

            for k in range(4):
                if center>0 and check[k] == center:
                    update_idx_set.add((i, j))
                    update_idx_set.add(pos[k])
                    flag = True

    if flag == True:
        for row, col in list(update_idx_set):
            plate[row][col] = 0
        return

    else:
        if cnt_ == 0:
            return
        mid = sum_/cnt_
        for i in range(1, N+1):
            for j in range(1, M+1):
                if plate[i][j] == 0:
                    continue
                if plate[i][j] < mid:
                    plate[i][j] = plate[i][j]+1
                elif plate[i][j] > mid:
                    plate[i][j] = plate[i][j]-1

def simulate():
    for idx, t in enumerate(turn):

        xnumber, direct, ktime = t
        # 회전
        for i in range(1, N+1):

            if i%xnumber == 0:
                rotate(i, direct, ktime)


        # 인접 확인, 갱신

        checkupdate()




N, M, T = map(int, input().split())
plate = dict()
turn = []
for i in range(1, N+1):
    data = [1001] + list(map(int, input().split()))
    plate[i] = deque(data)
for t in range(T):
    turn.append(list(map(int, input().split())))

simulate()
answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        answer += plate[i][j]
print(answer)