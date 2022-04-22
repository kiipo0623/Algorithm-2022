from collections import deque
maketree = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulate():
    for _ in range(K):
        # 봄울
        for i in range(N):
            for j in range(N):
                if tree[i][j] != 0:


        # 여름

        # 가을

        # 겨

N, M, K = map(int, input().split())
A = []
health = [[5]*N for _ in range(N)]
tree = [[deque()]*N for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

simulate()