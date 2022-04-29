from collections import deque
def lunch(teamA):
    teamB = [i for i in range(NUM) if i not in teamA]

    office = deque([])
    before_stair = deque([])
    stair = deque([])
    fin = 0
    time = 0

    for p in teamA:
        office.append([people_dis[p][0], 'A'])
    for p in teamB:
        office.append([people_dis[p][1], 'B'])

    while True:
        # 시간 흐르기
        time += 1
        if time >= result:
            return int(1e9)

        office = deque([[i[0]-1, i[1]] for i in office])
        before_stair = deque([[i[0] - 1, i[1]] for i in before_stair])
        stair = deque([[i[0] - 1, i[1]] for i in stair])

        # 단계 넘기기
        offlen = len(office)
        for _ in range(offlen):
            left, team = office.popleft()
            if left <= 0:
                before_stair.append([1, team])
            else:
                office.append([left, team])

        stlen = len(stair)
        canA, canB = 3, 3
        for _ in range(stlen):
            left, team = stair.popleft()
            if left <= 0:
                fin += 1
            else:
                if team == 'A':
                    canA -= 1
                elif team == 'B':
                    canB -= 1
                stair.append([left, team])

        waitlen = len(before_stair)
        for _ in range(waitlen):
            left, team = before_stair.popleft()
            if team == 'A':
                if canA>0 and left <= 0:
                    stair.append([stair_pos[0][2], team])
                    canA -= 1
                    continue

            if team == 'B':
                if canB>0 and left <= 0:
                    stair.append([stair_pos[1][2], team])
                    canB -= 1
                    continue

            before_stair.append([left, team])

        if fin == NUM:
            return time


def combination(select, maxnum):
    global result
    if len(select) == maxnum:
        t = lunch(select)
        # print("select ", select)
        # print("t ", t)
        result = min(t, result)
        return

    start = lst.index(select[-1])+1 if select else 0
    for i in range(start, NUM):
        select.append(i)
        combination(select, maxnum)
        select.pop()

def simulate():
    for i in range(NUM+1): # teamA에 0개부터 N개까지 선택
        combination([], i)
# import sys
# sys.stdin = open("sample_input.txt", 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = []
    stair_pos = []
    people_pos = []
    people_dis = [] # 각idx의 사람이 계단 A/B까지 걸리는 시간
    result = int(1e9)

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
    print("# {} {}".format(t, result))

