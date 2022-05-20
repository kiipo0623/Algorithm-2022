def solution(n, s, a, b, fares):
    answer = float('inf')
    dist = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for fare in fares:
        c, d, f = fare
        dist[c][d] = f
        dist[d][c] = f

    for i in range(1, n+1):
        dist[i][i] =0

    for k in range(1, n+1): #중간
        for i in range(1, n+1): # 시작
            for j in range(1, n+1): # 도착
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    print(dist)
    for node in range(1, n+1):
        answer = min(answer, dist[s][node] + dist[node][a] + dist[node][b])

    return answer

print(solution(
    # 6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    # 6,4,5,6,
))