def solve():
    N, A = int(input()), [0] + list(map(int, input().split()))
    S = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        S[i] = S[i-1] + A[i]

for _ in range(int(input())):
    solve()
