T = int(input())
for _ in range(T):
    K = int(input())
    page = list(map(int, input().split()))

    table = [[0]*K for _ in range(K)]

    # 누적합
    for i in range(K-1):
        table[i][i+1] = page[i] + page[i+1]
        for j in range(i+2, K):
            table[i][j] = table[i][j-1] + page[j]

    print(table)

    # 최종값
    for d in range(2, K):
        for i in range(K-d):
            j = i+d
            minimum = [table[i][t] + table[t+1][j] for t in range(i, j)]
            table[i][j] += min(minimum)

    print(table)
    print(table[0][K-1])