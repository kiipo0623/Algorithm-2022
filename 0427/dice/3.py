# UP RIGHT DOWN LEFT

dice = {
    'top':1,
    'bottom':6,
    'up':2,
    'down':5,
    'left':4,
    'right':3
}

def move_dice(x, y, d):
    global dice
    nx = x + dx[d]
    ny = y + dy[d]

    