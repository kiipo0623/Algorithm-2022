n = int(input())

chess_map = []
black = []
white = []
color = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        color[i][j] = (i%2 == 0 and j%2 == 0) or (i%2!=0 and j%2!=0)

for i in range(n):
    chess_map.append(list(map(int, input().split())))
    for j in range(n):
        if chess_map[i][j] == 1 and color[i][j] == 1:
            black.append((i, j))
        if chess_map[i][j] == 1 and color[i][j] == 0:
            white.append((i, j))

print(color)
print(black)
print(white)

bcnt = 0
wcnt = 0

isused01 = [0]*(n*2-1)
isused02 = [0]*(n*2-1)

def fun(bishop, index, count):
    global bcnt, wcnt
    if index == len(bishop):
        rx, ry = bishop[index-1]
        if color[rx][ry]:
            bcnt = max(bcnt, count)
        else:
            wcnt = max(wcnt, count)
        return

    x, y = bishop[index]
    if isused01[x+y] or isused02[x-y+n-1]:
        fun(bishop, index+1, count)
    else:
        isused01[x+y] = 1
        isused02[x-y+n-1] = 1
        fun(bishop, index+1, count+1)
        isused01[x+y] = 0
        isused02[x-y+n-1] = 0

if len(black):
    fun(black, 0, 0)
if len(white):
    fun(white, 0, 0)
print(bcnt+wcnt)