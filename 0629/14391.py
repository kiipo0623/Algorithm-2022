def bitmask():
    global maxAns
    for i in range(1<<N*M):
        total = 0
        # 가로 합 계산
        for row in range(N):
            rowsum = 0
            for col in range(M):
                # idx는 이차원 배열을 늘렸을 때 인덱스가 어디인지 의미
                idx = row * M + col
                # 가로일 때
                if i & (1 << idx) != 0:
                    rowsum = rowsum*10 + graph[row][col]
                # 세로일 때 앞에서 나온 수를 total에 더하고 rowsum 초기화
                else:
                    total += rowsum
                    rowsum = 0
            total += rowsum

        # 세로 합 계산
        for col in range(M):
            colsum = 0
            for row in range(N):
                idx = row * M + col
                if i & (1<<idx) == 0:
                    colsum = colsum * 10 + graph[row][col]
                else:
                    total += colsum
                    colsum = 0
            total += colsum

        maxAns = max(maxAns, total)

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))



