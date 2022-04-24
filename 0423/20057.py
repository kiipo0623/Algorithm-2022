# 좌 하 우 상
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

windpercent = [
    {(-2, 0):0.02, (-1, -1):0.1, (-1, 0):0.07, (-1, 1):0.01, (0, -2):0.05,
     (1, -1):0.1, (1, 0):0.07, (1, 1):0.01, (2, 0):0.02},
    {(-1, -1):0.01, (-1, 1):0.01, (0, -2):0.02, (0, -1):0.07, (0, 1):0.07, (0, 2):0.02,
    (1, -1):0.1, (1, 1):0.1, (2, 0):0.05},
    {(-2, 0): 0.02, (-1, -1):0.01, (-1, 0):0.07, (-1, 1):0.1, (0,2):0.05, (1, -1):0.01,
     (1, 0):0.07, (1, 1):0.1, (2, 0):0.02},
    {(-2, 0):0.05, (-1, -1):0.1, (-1, 1):0.1, (0, -2):0.02, (0, -1):0.07, (0, 1):0.07,
     (0, 2):0.02, (1, -1):0.01, (1, 1):0.01}
]

def tornado():
    global answer
    direct = -1
    tpos_x, tpos_y = N//2, N//2

    for i in range(N-1):
        for j in range(2):
            for k in range(1, N):
                direct = (direct + 1) % 4
                npos_x, npos_y = tpos_x+dx[direct], tpos_y+dy[direct]

                sand = board[npos_x][npos_y]
                board[npos_x][npos_y] = 0
                movesand = 0 # 알파 뺄때 쓸려고
                for wp_pos, percent in windpercent[direct].items():
                    wp_x, wp_y = wp_pos
                    wpos_x, wpos_y = npos_x+wp_x, npos_y+wp_y
                    now = int(sand * percent)
                    movesand += now
                    if wpos_x<0 or wpos_y<0 or wpos_x>=N or wpos_y>=N:
                        answer += now
                        print("answer ", answer, "now", now)
                    else:
                        board[wpos_x][wpos_y] += now
                print("npos", npos_x, npos_y)
                print("direct", direct, dx[direct], dy[direct])
                wpos_x, wpos_y = npos_x+dx[direct], npos_y+dy[direct]
                print("x, y", wpos_x, wpos_y)
                board[wpos_x][wpos_y] += (sand-movesand)
                tpos_x, tpos_y = npos_x, npos_y
                print(board)
    #
    # direct = (direct+1)%4
    # for i in range(N-1):
    #     npos_x, npos_y = tpos_x+dx[direct], tpos_y+dy[direct]
    #     sand = board[npos_x][npos_y]
    #     movesand = 0
    #     for wp_x, wp_y, percent in windpercent[direct].items():
    #         wpos_x, wpos_y = npos_x + wp_x, npos_y + wp_y
    #         movesand += sand * percent
    #         if wpos_x < 0 or wpos_y < 0 or wpos_x >= N or wpos_y >= N:
    #             answer += sand * percent
    #         else:
    #             board[wpos_x][wpos_y] += sand * percent
    #     wpos_x, wpos_y = npos_x + dx[direct], npos_y + dy[direct]
    #     board[wpos_x][wpos_y] += sand - movesand
    #     tpos_x, tpos_y = npos_x, npos_y
    #

N = int(input())
board = []
answer = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
tornado()

print(answer)