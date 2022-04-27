UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
dice = [
    [-1, 2, -1],
    [4, 1, 3],
    [-1, 5, -1],
    [-1, 6, -1]
]

def move_dice(dir):
    global dice
    if dir == RIGHT:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][3]