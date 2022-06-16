def solution(K, chp):
    DP = [[0 for _ in range(K+1)] for _ in range(K+1)]
    S = [sum(chp[:i]) for i in range(K+1)]

    for length in range(1, K): # 시작점에서 몇칸 떨어져 있는지
        for idx in range(1, K-length+1): # 시작점 후보
            minn = int(1e9)
            for checker in range(idx,idx+length):
                minn = min(minn, DP[idx][checker] + DP[checker+1][idx+length])
            DP[idx][idx+length] = minn + (S[idx+length] - S[idx-1])

    return DP[1][K]

T = int(input())
for _ in range(T):
    K = int(input())
    chapter = list(map(int, input().split()))
    print(solution(K, chapter))