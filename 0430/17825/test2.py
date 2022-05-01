def bt(horse, idx, grade):
    # print("horse ", horse)
    # print("idx ", idx)
    # print("grade ", grade)
    # print()
    global answer
    if idx == 10:
        answer = max(answer, grade)
        return

    # 0,0에 여러 개 있는 경우
    startflag = False
    for i in range(4):
        row, col = horse[i]

        # 0번째 처리
        if row == 0 and col == 0:
            if startflag == True:
                continue
            else:
                startflag = True

        # 마지막 위치면 이동 불가
        if (row, col) in same_place[0]:
            continue

        drow, dcol = row, col + dice[idx]

        # 예외처리 : 도착지점 넘는 경우
        if dcol > len(board[drow])-1:
            # print("마지막 위치 예외 ", idx)
            # print(drow, dcol)
            dcol = len(board[drow])-1

        # 마지막 위치인 경우 : continue하면 안됨!
        # if (drow, dcol) in same_place[0]:
        #     # print("마지막 dnlcl ", idx)
        #     # print(drow, dcol)
        #     continue

        # 도착 지점을 갈 수 있는지?
        if [drow, dcol] in horse and (drow, dcol) not in same_place[0]: # 다른 말 존재
            continue
        if board[drow][dcol] in same_place.keys(): # 확인 요망
            # print("확인 요망")
            # print(drow, dcol, board[drow][dcol])
            for r, c in same_place[board[drow][dcol]]:
                if [r, c] in horse:
                    continue

        # 해당 안되면 이동!
        # 파란색 시작 처리
        if board[drow][dcol] in blueflag.keys():
            drow, dcol = blueflag[board[drow][dcol]]
            print(drow, dcol)

        horse[i] = [drow, dcol]
        get = board[drow][dcol]
        bt(horse, idx+1, grade+get)
        horse[i] = [row, col]


dice = list(map(int, input().split()))
horse = [[0,0], [0,0], [0,0], [0,0]]

answer = 0

blueflag = {10:[1, 0], 20:[2, 0], 30:[3, 0]}

default = [i for i in range(0, 41, 2)] + [0]
ten = [10, 13, 16, 19, 25, 30, 35, 40, 0]
twenty = [20, 22, 24, 25, 30, 35, 40, 0]
thirty = [30, 28, 27, 26, 25, 30, 35, 40, 0]
board = [default, ten, twenty, thirty]
print(board)
print(board[0][15])

# 마지막은 아직 처리 못함
same_place = {10:[(0, 5), (1, 0)],
              20:[(0, 10), (2, 0)],
              30:[(0, 15), (3, 0)],
              25:[(1, 4), (2, 3), (3, 4)],
              40:[(0, 20), (1, 7), (2, 6), (3, 7)],
              0:[(0, 21), (1, 8), (2, 7), (3, 8)]
              }

bt(horse, 0, 0)
print(answer)
# 'fin':[(0, 21), (1, 8), (2, 7), (3, 8)]