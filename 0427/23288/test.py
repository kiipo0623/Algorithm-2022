# 0up 1top 2dowm 3bottom 4left 5right
dice = [2,1,5,6,4,3]

def dice_move(d):
    # RIGHT DOWN LEFT UP
    if d==0: # RIGHT
        # left top right bottom = bottom left top right
        dice[4], dice[1], dice[5], dice[3] = dice[3], dice[4], dice[1], dice[5]
    elif d==1: # DOWN
        # up top down bottom = bottom up top down
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    elif d==2: # LEFT
        # left top right bottom = top right bottom left
        dice[4], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[4]
    elif d==3: # UP
        # up top down bottom = top down bottom up
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]