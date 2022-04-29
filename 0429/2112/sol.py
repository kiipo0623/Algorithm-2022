T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split() for _ in range(D)))]
    raw = [f[:] for f in film]
