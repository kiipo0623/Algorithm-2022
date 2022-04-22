from collections import deque
from copy import deepcopy
N, M, K = map(int, input().split())
maketree = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulate(treequeue):
    for i in range(K):
        # 봄 여름
        queue = deepcopy(treequeue)
        newqueue = deque()
        while queue:
            row, col = queue.popleft()
            treeagequeue = tree[row][col]
            treeagequeue = deque(sorted(treeagequeue))
            newtreeagequeue = deque()
            while treeagequeue:
                age = treeagequeue.popleft()
                if health[row][col] >= age:
                    health[row][col] -= age
                    age += 1
                    newtreeagequeue.append(age)
                    if age%5 == 0:
                        age5queue.append((row, col, age))
                else:
                    health[row][col] += age//2
            tree[row][col] = deepcopy(newtreeagequeue)
            if len(newtreeagequeue) != 0:
                newqueue.append([row, col])
        treequeue = deepcopy(newqueue)

        if age5queue:
            while age5queue:
                row, col, age = age5queue.popleft()
                for make in maketree:
                    trow = row + make[0]
                    tcol = col + make[0]
                    tree[trow][tcol].append(1)

        # 겨울
        for i in range(N):
            for j in range(N):
                health[i][j] += A[i][j]

        if len(treequeue) == 0:
            return


A = []
health = [[5]*N for _ in range(N)]
tree = [[deque()]*N for _ in range(N)]
treequeue = deque()
age5queue = deque()

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)
    if [x-1, y-1] not in treequeue:
        treequeue.append([x-1, y-1])

simulate(treequeue)

print(len(treequeue))