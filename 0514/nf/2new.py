import heapq
def dijkstra(start, N):
    global connect
    INF = 101
    h = []
    heapq.heappush(h, (0, start))
    dist = [INF]*N
    dist[start] = 0

    while h:
        dis, now = heapq.heappop(h)
        if dis < dist[now]:
            continue

        for node, cost in connect[now]:
            cost += dis
            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(h, (cost, node))
    return dist

def solution(cities, roads, cars, customers):
    global distance, connect
    answer = []
    INF = 101
    WEI = 10001

    city_idx = dict()
    idx_city = dict()
    distance = [[INF] * len(cities) for _ in range(len(cities))]
    truck = {i:[WEI]*WEI for i in range(len(cities))}
    min_weight = {i:WEI for i in range(len(cities))}
    connect = [[] for _ in range(len(cities))]

    for idx, city in enumerate(cities):
        city_idx[city] = idx
        idx_city[idx] = city
    print(idx_city)

    for road in roads:
        start, end, dis = road.split()
        s = city_idx[start]
        e = city_idx[end]
        dis = int(dis)
        distance[s][e] = dis
        distance[e][s] = dis
        connect[s].append((e, dis))
        connect[e].append((s, dis))

    for i in range(len(cities)):
        res = dijkstra(i, len(cities))
        for j in range(len(cities)):
            distance[i][j] = res[j]
    # 거리 완료

    for car in cars:
        car_city, car_weight, car_1km = car.split()
        car_weight, car_1km = int(car_weight), int(car_1km)
        car_city = city_idx[car_city]
        truck[car_city][car_weight] = car_1km
        if min_weight[car_city] > car_weight:
            min_weight[car_city] = car_weight



    for customer in customers:
        cus_start, cus_end, cus_weight = customer.split()
        cus_start, cus_end = city_idx[cus_start], city_idx[cus_end]
        cus_weight = int(cus_weight)

        use_city, min_cost = -1, float('inf')
        for city in range(len(cities)):
            if min_weight[city] >= cus_weight and distance[city][cus_start] != INF: # 가능한 차가 있으면
                money = WEI
                for i in range(cus_weight, WEI):
                    if truck[city][i] < WEI:
                        money = truck[city][i]
                        break
                cost = (distance[city][cus_start] + distance[cus_start][cus_end]) * money
                print("city", city, "money", money, "cost",cost, "min_cost, ")
                if cost<min_cost:
                    use_city, min_cost = city, cost
                elif cost == min_cost:
                    if idx_city[use_city] > idx_city[city]: # 새 도시가 빠름
                        use_city, min_cost = city, min_cost

        print(use_city)
        answer.append(idx_city[use_city])
        print()

    return answer


# print(solution(
# ["a","b","c"],
# ["a b 1","a c 1","b c 1"],
# ["a 100 10","b 300 20","c 50 4"],
# ["a b 100","a b 30","c a 250"]
# ))

print(solution(
["a","b","c","d","e","f","g"],
["a b 1","a c 1","c d 3","b d 5","b e 6","d e 2","f g 8"],
["a 100 10","a 200 15","b 100 5","c 20 2","c 300 30","d 200 20","e 500 100","f 500 50","g 100 40"],
["g f 200","c e 50","d a 500","a b 50"],

))