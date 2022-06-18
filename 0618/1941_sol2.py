dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(num):
    global available, visited
    r = num // 5
    c = num % 5

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if not (0 <= nr < 5 and 0 <= nc < 5) or visited[nr][nc]:
            continue

        nextNum = nr*5 + nc
        if nextNum in p:
            visited[nr][nc] = 1
            available += 1
            check(nextNum)

def dfs(depth, ycnt, idx):
    global result, available, visited
    if ycnt > 3 or 25-idx < 7-depth:
        return

    if depth == 7:
        available = 1
        visited = [[0]*5 for _ in range(5)]
        sr, sc = p[0]//5, p[0]%5
        visited[sr][sc] = 1
        check(p[0])
        if available == 7:
            result += 1
        return

    r = idx // 5
    c = idx % 5

    if A[r][c] == "Y":
        p.append(idx)
        dfs(depth+1, ycnt+1, idx+1)
        p.pop()

    elif A[r][c] == "S":
        p.append(idx)
        dfs(depth+1, ycnt, idx+1)
        p.pop()

    dfs(depth, ycnt, idx+1)



A = [input().rstrip() for _ in range(5)]
visited = [[0] for _ in range(5) for _ in range(5)]
result = 0
p = []
dfs(0, 0, 0)
print(result)