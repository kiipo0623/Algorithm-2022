from collections import deque, defaultdict
maketree = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulate():
    global treelist
    for i in range(K):
        # 봄 여름
        for tree in treelist:
            row, col = tree
            queue = treelist[tree]
            newqueue = deque([])

            while queue:
                age = queue.popleft()
                if health[row][col] >= age:
                    health[row][col] -= age
                    age += 1
                    newqueue.append(age)
                    if age%5 == 0:
                        age5list.append((row, col, age))
                else:
                    health[row][col] += age//2
            treelist[tree] = newqueue

        # 가을
        if age5list:
            while age5list:
                row, col, age = age5list.popleft()
                for make in maketree:
                    trow = row + make[0]
                    tcol = col + make[0]
                    treelist[trow][tcol].append(1)

        #겨울
        for i in range(N):
            for j in range(N):
                health[i][j] += A[i][j]



N, M, K = map(int, input().split())

A = []
health = [[5]*N for _ in range(N)]
tree = [[[]]*N for _ in range(N)]
treelist = defaultdict(deque)
age5list = deque()

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    x, y, z = map(int, input().split())
    treelist[(x-1, y-1)].append(z)

simulate()

print(len(treelist))