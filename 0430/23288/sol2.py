from collections import deque
# 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 0back 1up 2front 3down 4left 5right
dice = [2, 1, 5, 6, 4, 3]

def move_dice(dir):
    # 동쪽
    if dir == 0:
        dice[3], dice[5], dice[1], dice[4] = dice[5], dice[1], dice[4], dice[3]
    # 남쪽
    elif dir == 1:
        dice['down'], dice['front'], dice['up'], dice['back'] = dice['front'], dice['up'], dice['back'], dice['down']
    # 서쪽
    elif dir == 2:
        dice['down'], dice['left'], dice['up'], dice['right'] = dice['left'], dice['up'], dice['right'], dice['down']
    # 북쪽
    elif dir == 3:
        dice['back'], dice['up'], dice['front'], dice['down'] = dice['up'], dice['front'], dice['down'], dice['back']

move_dice(0)
print(dice)