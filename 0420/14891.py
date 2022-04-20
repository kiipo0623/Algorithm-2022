from collections import deque

def checkNS():
    # 같으면 False(안해도됨) 다르면 True(해야됨)
    NS = [False]
    if graph[1][2]==graph[2][6]:
        NS.append(False)
    else:
        NS.append(True)

    if graph[2][2]==graph[3][6]:
        NS.append(False)
    else:
        NS.append(True)

    if graph[3][2]==graph[4][6]:
        NS.append(False)
    else:
        NS.append(True)

    return NS

def checkmovecand(num, dir):
    sunseo = [(num, dir)]
    # 앞 확인
    beforedir = dir
    for i in range(num, 1, -1):
        if graph[i][6]==graph[i-1][2]: # 같으면
            break
        else:
            beforedir = beforedir * (-1)
            sunseo.append((i-1, beforedir))
    # 뒤 확인
    beforedir = dir
    for i in range(num, 4):
        if graph[i][2] == graph[i+1][6]:
            break
        else:
            beforedir = beforedir * (-1)
            sunseo.append((i+1, beforedir))
    return sunseo


def movequeue(turn, dir): # 큐 이동
    if dir == 1: # 시계방향
        now = graph[turn].pop()
        graph[turn].appendleft(now)
    elif dir == -1: # 반시계방향
        now = graph[turn].popleft()
        graph[turn].append(now)

def countgrade(): # 점수 계산
    sum_ = 0
    if graph[1][0] == '1':
        sum_ += 1
    if graph[2][0] == '1':
        sum_ += 2
    if graph[3][0] == '1':
        sum_ += 4
    if graph[4][0] == '1':
        sum_ += 8
    return sum_

graph = [[]]
for _ in range(4):
    graph.append(deque(list(input())))

K = int(input())
for _ in range(K):
    number, direction = map(int, input().split())
    sunseo = checkmovecand(number, direction)
    for s in sunseo:
        tempturn, tempdir = s
        movequeue(tempturn, tempdir)

print(countgrade())

