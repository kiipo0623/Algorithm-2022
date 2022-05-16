import heapq
from collections import defaultdict

MAX_DIS = 101
def dijkstra(start):
    global city_mindis, NCITY
    h = []
    heapq.heappush(h, (0, start))
    distance = [MAX_DIS] * NCITY
    distance[start] = 0

    while h:
        dis, now = heapq.heappop(h)
        if dis > distance[start]:
            continue

def solution(cities, roads, cars, customers):
    global city_mindis, NCITY
    answer = []
    NCITY = len(cities)

    city_index = defaultdict(int)
    index_city = defaultdict(str)

    city_truck = dict()
    city_mindis = [[MAX_DIS] * NCITY for _ in range(NCITY)]

    graph = [[] for _ in range(NCITY)]

    idx = 0
    for road in roads:

        start, end, distance = road




    for i in range(NCITY):
        dijkstra(i)


    return answer