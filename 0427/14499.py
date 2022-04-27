dice = {
    'top':0, 'bottom':0, 'up':0, 'down':0, 'left':0, 'right':0
}
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
def move_dice(dir):
    if dir == 1: # 오른쪽
        dice['left'], dice['bottom'], dice['right'], dice['top'] = dice['top'], dice['left'], dice['bottom'], dice['right']
    elif dir == 2: # 왼쪽
        dice['left'], dice['bottom'], dice['right'], dice['top'] = dice['bottom'], dice['right'], dice['top'], dice['left']
    elif dir == 3: # 위쪽
        dice['up'], dice['bottom'], dice['down'], dice['top'] = dice['bottom'], dice['down'], dice['top'], dice['up']
    elif dir == 4: # 아래쪽
        dice['up'], dice['bottom'], dice['down'], dice['top'] = dice['top'], dice['up'], dice['bottom'], dice['down']
def checkout(row, col):
    if row<0 or row>=N or col<0 or col>=M:
        return True
    else:
        return False
def simulate():
    global x, y
    for do in todo:
        drow, dcol = x + dx[do], y + dy[do]
        if checkout(drow, dcol):
            continue
        move_dice(do)
        x, y = drow, dcol
        if board[x][y] == 0:
            board[x][y] = dice['bottom']
        else:
            dice['bottom'] = board[x][y]
            board[x][y] = 0
        print(dice['top'])

N, M, x, y, K = map(int, input().split())
board= []
for _ in range(N):
    board.append(list(map(int, input().split())))
todo = list(map(int, input().split()))
simulate()