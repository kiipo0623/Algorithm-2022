T = int(input())
for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))
    DP = [[0 for _ in range(K+1)] for _ in range(K+1)]
    tmp = [sum(pages[:i]) for i in range(K+1)]

    # DP[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    # DP[i][k] + DP[k+1][j] + sum(A[i]~A[j])
    for j in range(2, K+1): # 길이
        for i in range(1, K+2-j): # 시작점
            m = int(1e9)
            for k in range(j-1): # 합치는 지점 거리(시작점으로부터)
                m = min(m, DP[i][i+k] + DP[i+k+1][i+j-1])
            DP[i][i+j-1] = m + (tmp[i+j-1] - tmp[i-1])

    print(DP)
    print(DP[1][K])