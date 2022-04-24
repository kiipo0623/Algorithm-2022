from copy import deepcopy
movedir = {1:(-1, 0), 2:(-1, -1), 3:(0, -1), 4:(1, -1), 5:(1, 0), 6:(1, 1), 7:(0, 1), 8:(-1, 1)}

def move_fish(pool, fishdict):
    for fishnum in range(1, 17):
        if fishdict[fishnum] == False: # 물고기 죽었으면 패스
            continue

        row, col = fishdict[fishnum]
        _, fishdir = pool[row][col]

        for i in range(8):
            # 이동 시도
            drow, dcol = row+movedir[fishdir][0], col+movedir[fishdir][1]
            if drow<0 or drow>=4 or dcol<0 or dcol>=4 or pool[drow][dcol][0] == -1:
                fishdir = (fishdir+1)%9
                if fishdir == 0:
                    fishdir = 1
            elif pool[drow][dcol] == [0, 0]:
                pool[drow][dcol] = [fishnum, fishdir]
                pool[row][col] = [0, 0]
                fishdict[fishnum] = [drow, dcol]
                break
            else:
                diff_fish_num = pool[drow][dcol][0] # 상대 물고기 번호 받아옴
                pool[row][col][1] = fishdir # 내 물고기 방향 전환
                pool[row][col], pool[drow][dcol] = pool[drow][dcol], pool[row][col] # 어항 swap
                fishdict[fishnum] = [drow, dcol] #  내 물고기 갱신
                fishdict[diff_fish_num] = [row, col] # 상대 물고기 갱신
                break

    return pool, fishdict

def bt_shark(graph, shark_row, shark_col, grade, fishdict, depth):
    global answer
    # 방향 받아와서 후보 탐색
    shark_dir = graph[shark_row][shark_col][1]
    shark_move_cand = []
    # 방향 전환 위해서
    temp_row, temp_col = shark_row, shark_col

    while True:
        drow, dcol = temp_row+movedir[shark_dir][0], temp_col+movedir[shark_dir][1]
        if drow<0 or drow>=4 or dcol<0 or dcol>=4:
            break
        elif graph[drow][dcol] == [0, 0]:
            temp_row, temp_col = drow, dcol
            continue
        else:
            temp_row, temp_col = drow, dcol
            shark_move_cand.append([drow, dcol])

    if len(shark_move_cand) == 0:
        answer = max(answer, grade)
        return

    # 상어 잡아먹는 과정
    for cand_row, cand_col in shark_move_cand:
        fish_num, fish_dir = graph[cand_row][cand_col]
        fishdict[fish_num] = False # 물고기 사전 갱신
        graph[shark_row][shark_col] = [0, 0] # 상어 원래 자리
        graph[cand_row][cand_col] = [-1, fish_dir] # 물고기 원래 자리
        temp_board, temp_dict = move_fish(deepcopy(graph), deepcopy(fishdict))
        bt_shark(temp_board, cand_row, cand_col, grade + fish_num, temp_dict, depth+1)
        fishdict[fish_num] = [cand_row, cand_col] # 물고기 사전 초기화
        graph[shark_row][shark_col] = [-1, shark_dir] # 상어 자리 초기화
        graph[cand_row][cand_col] = [fish_num, fish_dir]

fishdict = dict()
board = [[False]*(4) for _ in range(4)]
answer = 0

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(0, 8, 2):
        num = data[j]
        fishdict[num] = [i, j//2]
        board[i][j//2] = [num, data[j+1]]

# 상어 초기 설정
diefishnum, diefishdir = board[0][0]
board[0][0] = [-1, diefishdir]
fishdict[diefishnum] = False


new_board, new_dict = move_fish(board, fishdict)

bt_shark(new_board, 0, 0, diefishnum, new_dict, 0)

print(answer)