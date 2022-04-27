direct = {1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
d = 1
s = 3
N = 5
row = 3
col = 0

for _ in range(s):
    drow, dcol = row + direct[d][0], col + direct[d][1]
    if drow==0:
        drow = N - 1
    elif drow == N:
        drow = 0
    if dcol == -1:
        dcol = N - 1
    elif dcol == N:
        dcol = 0
    row, col = drow, dcol

print(drow, dcol)

row = 3
col = 0

nx = (s * direct[d][0] + row) % N
print(s * direct[d][1] + col)
ny = (s * direct[d][1] + col) % N
print(-3%5)
print(nx, ny)