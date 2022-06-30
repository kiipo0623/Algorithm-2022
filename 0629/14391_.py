def bitmask():
    max_sum = 0
    # 가로:1 세로:0 으로 가정
    for idx in range(1<<n*m):
        print(bin(idx))
        idx_sum = 0
        # 가로 계산
        for row in range(n):
            total = 0
            for col in range(m):
                now = row*m+col
                # 둘다 1이면 가로
                if idx & (1 << now) != 0:
                    total = total*10 + graph[row][col]
                else:
                    idx_sum += total
                    total = 0
            idx_sum += total

        # 세로 계산
        for col in range(m):
            total = 0
            for row in range(n):
                now = row * m+ col
                if idx & (1 << now) == 0:
                    total = total*10 + graph[row][col]
                else:
                    idx_sum += total
                    total = 0
            idx_sum += total

        max_sum = max(max_sum, idx_sum)
    return max_sum


n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
print(graph)
print(bitmask())
