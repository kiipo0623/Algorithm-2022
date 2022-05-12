import sys
input = sys.stdin.readline
INF = 10001

def bellman_ford(start):
    distance = {i:INF for i in range(1, N+1)}
    distance[start] = 0

    for _ in range(N-1): # 그냥 이만큼 해야 된다
        for node in range(1, N+1): # 중간 지점
            for neighbor in range(1, N+1):
                distance[neighbor] = min(distance[neighbor], distance[node]+road[node][neighbor])
            for neighbor in range(1, N+1):
                if wormhall[node][neighbor] != INF:
                    distance[neighbor] = min(distance[neighbor], distance[node]-wormhall[node][neighbor])
    #
    # print(distance)
    # worm 타고 마이너스 되는 경우
    for i in range(1, N+1):
        if wormhall[i][start] != INF and i != start:
            if distance[i] - wormhall[i][start] < 0:
                return True
    # 원래 마이너스 여서 해결되는 경우
    for i in range(1, N+1):
        if road[i][start] != INF and i != start:
            if distance[i] + road[i][start] < 0:
                return True
    return False

def time_travel():
    if bellman_ford(1):
        return True
    return False

TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    road = [[INF]*(N+1) for _ in range(N+1)] # 양방향
    wormhall = [[INF]*(N+1) for _ in range(N+1)] # 단방향

    for _ in range(M):
        S, E, T = map(int, input().split())
        road[S][E] = T
        road[E][S] = T

    for _ in range(W):
        S, E, T = map(int, input().split())
        wormhall[S][E] = T

    if time_travel():
        print("YES")
    else:
        print("NO")
