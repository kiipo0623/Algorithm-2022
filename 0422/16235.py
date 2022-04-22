from collections import deque, defaultdict

baby = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def simulate():
    dietreequeue = defaultdict(list)
    age5queue = deque([])
    for _ in range(K):
        #봄
        for i in range(len(treequeue)):
            npos_x, npos_y = treequeue.popleft()
            die_index = -1
            for idx, age in enumerate(tree[npos_x][npos_y]):
                if health[npos_x][npos_y] >= age:
                    health[npos_x][npos_y] -= age
                    age += 1
                    tree[npos_x][npos_y][idx] = age
                    if (npos_x, npos_y) not in treequeue:
                        treequeue.append((npos_x, npos_y))
                    if age %5 == 0:
                        age5queue.append((npos_x, npos_y))
                else:
                    dietreequeue[(npos_x, npos_y)].append(age)
                    die_index = idx

            if die_index != -1:
                if die_index == 0:
                    tree[npos_x][npos_y] = False
                else:
                    tree[npos_x][npos_y] = tree[npos_x][npos_y][:idx]
        # 여름
        for key, value in dietreequeue.items():
            for v in value:
                health[key[0]][key[1]] += (v//2)

        # 가을
        while age5queue:
            npos_x, npos_y = age5queue.popleft()
            for b in baby:
                dpos_x, dpos_y = npos_x+b[0], npos_y+b[1]
                if 0<=dpos_x<N and 0<=dpos_y<N:
                    if (dpos_x, dpos_y) not in treequeue:
                        treequeue.append((dpos_x, dpos_y))
                        tree[dpos_x][dpos_y] = [1]
                    else:
                        tree[dpos_x][dpos_y].insert(0, 1)
        #겨울
        for i in range(N):
            for j in range(N):
                health[i][j] += A[i][j]

N, M, K = map(int, input().split())
A = []

health = [[5]*N for _ in range(N)] # 양분
tree = [[False]*N for _ in range(N)] # 나무
treequeue = deque([])

for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    x, y, z = map(int, input().split())
    tree[x-1][y-1] = [z]
    treequeue.append((x-1, y-1))
answer = 0
simulate()

for i in range(N):
    for j in range(N):
        if tree[i][j] != False:
            answer += len(tree[i][j])

print(answer)