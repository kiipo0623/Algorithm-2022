from math import exp
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
happy = {0:0, 1:1, 2:10, 3:100, 4:1000}
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

def simulate():
    global answer
    global board
    for do in todo:
        student = do.pop(0)
        tmp = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    like, empty = 0, 0
                    for k in range(4):
                        drow, dcol = i+dx[k], j+dy[k]
                        if checkout(drow, dcol):
                            continue
                        elif board[drow][dcol] in do:
                            like += 1
                        elif board[drow][dcol] == 0:
                            empty += 1
                tmp.append((like, empty, i, j))

        tmp.sort(key = lambda x : (-x[0], -x[1], x[2], x[3]))
        for _, _, row, col in tmp:
            if board[row][col] == 0:
                board[row][col] = student
                break


    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                drow, dcol = i+dx[k], j+dy[k]
                if checkout(drow, dcol) == False and board[drow][dcol] in student_like[board[i][j]]:
                    cnt += 1
            answer += happy[cnt]


N = int(input())
todo = []
board = [[0]*N for _ in range(N)]
answer = 0
student_like = dict()
for _ in range(N**2):
    data = list(map(int, input().split()))
    todo.append(data)
    student_like[data[0]] = data[1:]
simulate()
print(answer)