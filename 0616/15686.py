from itertools import combinations

N, M = map(int, input().split())
graph = []
chicken = []
home = []

for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j] == 1:
            home.append((i, j))
        elif tmp[j] == 2:
            chicken.append((i, j))
    graph.append(tmp)

select = list(combinations(chicken, M))
answer = int(1e9)
for combi in select:
    summ = 0
    for h in home:
        minn = int(1e9)
        for c in combi:
            minn = min(minn, abs(c[0]-h[0]) + abs(c[1]-h[1]))
        summ += minn
    answer = min(summ, answer)
print(answer)
