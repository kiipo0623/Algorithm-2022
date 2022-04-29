from collections import deque
def lunch(teamA):
    teamB = [i for i in range(NUM) if i not in teamA]

    teamA_walk, teamB_walk = deque([]), deque([])
    teamA_stair_wait, teamB_stair_wait = deque([]), deque([])
    teamA_stair_go, teamB_stair_go = deque([]), deque([])
    fin = 0

    for p in teamA:
        teamA_walk.append(people_dis[p][0])
    for p in teamB:
        teamB_walk.append(people_dis[p][1])

    time = 0
    while True:
        time += 1 # 시간 흐름
        teamA_walk = [i-1 for i in teamA_walk]
        teamB_walk = [i-1 for i in teamB_walk]
        teamA_stair_wait = [i-1 for i in teamA_stair_wait]
        teamB_stair_wait = [i-1 for i in teamB_stair_wait]
        teamA_stair_go = [i-1 for i in teamA_stair_go]
        teamB_stair_go = [i-1 for i in teamB_stair_go]

        # 사무실 -> 계단대기
        mvA = teamA_walk.count(0)
        mvB = teamB_walk.count(0)
        while 0 in teamA_walk:
            teamA_walk.remove(0)
        while 0 in teamB_walk:
            teamB_walk.remove(0)
        teamA_stair_wait.extend([1]*mvA)
        teamB_stair_wait.extend([1]*mvB)
        # 계단 -> 종료
        mvA = teamA_stair_go.count(0)
        mvB = teamB_stair_go.count(0)
        while 0 in teamA_stair_go:
            teamA_stair_go.remove(0)
        while 0 in teamB_stair_go:
            teamB_stair_go.remove(0)
        fin += mvA
        fin += mvB

        # 계단대기 -> 계단
        mvA = teamA_walk.count(0)
        mvB = teamB_walk.count(0)

        canA = 3-len(teamA_stair_go)
        canB = 3-len(teamB_stair_go)

        # 다가는 경우 / 하나도 못가는 경우 / 일부 가는 경우
        if canA - mvA < 0:
            teamA_stair_go.extend([stair_pos[0][2]]*mvA)
        elif canA-mvA >= 0: # 일부 가는 경우









def combination(select, maxnum):
    if len(select) == maxnum:
        lunch(select)
        return

    start = lst.index(select[-1])+1 if select else 0
    for i in range(start, NUM):
        select.append(i)
        combination(select, maxnum)
        select.pop()

def simulate():
    for i in range(NUM+1): # teamA에 0개부터 N개까지 선택
        print("----",i)
        combination([], i)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    stair_pos = []
    people_pos = []
    people_dis = [] # 각idx의 사람이 계단 A/B까지 걸리는 시간

    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(N):
            if data[j] == 1:
                people_pos.append((i, j))
            elif data[j]>1:
                stair_pos.append((i, j, data[j]))
        board.append(data)

    for p in people_pos:
        tmp = []
        for s in stair_pos:
            dis = abs(s[0]-p[0]) + abs(s[1]-p[1])
            tmp.append(dis)
        people_dis.append(tmp)

    NUM = len(people_pos)
    lst = [i for i in range(NUM)]
    simulate()


