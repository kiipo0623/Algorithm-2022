def road(row):
    visit = [False]*len(row)
    if len(set(row)) == 1: # 전부 같은 경우
        return True

    for i in range(1, N):
        if row[i-1] == row[i]: # 같은 경우
            continue

        if row[i-1]+1 != row[i] and row[i-1]-1 != row[i]: # 1이상 차이나는 경우
            return False

        else: # 1차이나는 경우
            if row[i-1] < row[i]: # 앞이 작은 경우
                if True in visit[i-L:i] or i-L<0 or len(set(row[i-L:i])) != 1: # L만큼 같은 높이 지속되지 않음
                    return False
                else:
                    for k in range(i-L, i, 1):
                        visit[k] = True

            else: # 뒤가 작은 경우
                if True in visit[i:i+L] or i+L>len(row) or len(set(row[i:i+L])) != 1: # L만큼 같은 높이 지속되지 않음
                    return False
                else:
                    for k in range(i, i+L, 1):
                        visit[k] = True
    return True

N, L = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
answer = 0

for i in range(N):
    if road(graph[i]): answer += 1

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(graph[j][i])
    if road(temp): answer += 1

print(answer)