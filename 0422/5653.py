from copy import deepcopy
import sys
# sys.stdin = open("sample_input.txt", "r")
T = int(input())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def simulate(startrow, startcol, endrow, endcol):
    global stategraph, cntgraph, lifegraph
    for time in range(K):
        tempstate, tempcnt = [['N']*(K+M+K) for _ in range(K+N+K)], [[0]*(K+M+K) for _ in range(K+N+K)]
        for i in range(startrow-1, endrow):
            for j in range(startcol-1, endcol):
                # 아무것도 아닐 때 : 사방 확인
                if stategraph[i][j] == 'N':
                    max_ = -1
                    for dir in range(4):
                        pos_x, pos_y = i+dx[dir], j+dy[dir]
                        if 0<=pos_x<(N+K+K) and 0<=pos_y<(M+K+K):
                            if stategraph[pos_x][pos_y] == 'T':
                                max_ = max(max_, lifegraph[pos_x][pos_y])

                    if max_ != -1:
                        lifegraph[i][j] = max_
                        tempstate[i][j] = 'F'
                        tempcnt[i][j] = max_*2

                # 죽었을 때 : 패스
                elif stategraph[i][j] == 'D':
                    tempstate[i][j] = 'D'

                # 활성화일 때 : 나이먹기
                elif stategraph[i][j] == 'T':
                    tempcnt[i][j] = cntgraph[i][j]-1
                    tempstate[i][j] = 'T'

                    if tempcnt[i][j] == 0:
                        tempstate[i][j] = 'D'

                # 비활성화일 때 : 나이먹기
                elif stategraph[i][j] == 'F':
                    tempcnt[i][j] = cntgraph[i][j] - 1
                    tempstate[i][j] = 'F'

                    if tempcnt[i][j] == lifegraph[i][j]:
                        tempstate[i][j] = 'T'

        stategraph, cntgraph = deepcopy(tempstate), deepcopy(tempcnt)
        startrow, startcol, endrow, endcol = startrow-1, startcol-1, endrow+1, endcol+1


for tc in range(T):
    N, M, K = map(int, input().split())
    stategraph = [['N']*(K+M+K) for _ in range(K+N+K)]
    lifegraph = [[0]*(K+M+K) for _ in range(K+N+K)]
    cntgraph = [[0]*(K+M+K) for _ in range(K+N+K)]

    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(M):
            if data[j] != 0:
                lifegraph[i+K][j+K] = data[j]
                cntgraph[i+K][j+K] = data[j]*2
                stategraph[i+K][j+K] = 'F'

    simulate(K, K, K+N, K+M)
    answer = 0
    for i in range(K+N+K):
        answer += stategraph[i].count('T')
        answer += stategraph[i].count('F')
    print("#%d %d"%(tc+1, answer))


