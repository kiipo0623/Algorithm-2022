dice = {'back': 2, 'up': 1, 'front': 5, 'down': 6, 'left': 4, 'right': 3}


def can_move(row, col, dir):
    if dir == 0 and col >= M:
        return 2
    if dir == 1 and row >= N:
        return 3
    if dir == 2 and col < 0:
        return 0
    if dir == 3 and row < 0:
        return 1
    else:
        return dir


def move_dice(dir):
    # 동쪽
    if dir == 0:
        dice['down'], dice['right'], dice['up'], dice['left'] = dice['right'], dice['up'], dice['left'], dice['down']

    # 서쪽
    elif dir == 2:
        dice['down'], dice['left'], dice['up'], dice['right'] = dice['left'], dice['up'], dice['right'], dice['down']

N, M = 4, 5
move_dice(0)
print(dice)