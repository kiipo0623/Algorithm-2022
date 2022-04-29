N = 5
move_cnt = []
# L D R U
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
for i in range(1, N+1):
    move_cnt.extend([i,i])
move_queue = []

row, col = N//2, N//2
cnt = 0
print(move_cnt)

def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=N:
        return True
    return False

while not checkout(row, col):
    direct = cnt%4
    iter = move_cnt[cnt]
    for _ in range(iter):
        drow, dcol = row + dx[direct], col + dy[direct]
        move_queue.append((drow, dcol))
        row, col = drow, dcol
    cnt += 1

r