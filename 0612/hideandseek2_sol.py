from collections import deque

def bfs(start):
    global result
    q = deque()
    q.append(start)
    arr[start] = 0
    while q:
        x = q.popleft()
        if x == K:
            result += 1
            continue
        for nx in (x*2, x+1, x-1):
            if 0 <= nx < 100001 and (arr[nx] == arr[x] + 1 or arr[nx] == -1):
                arr[nx] = arr[x] + 1
                q.append(nx)


N, K = map(int, input().split())
arr = [-1] * 100001
result = 0

bfs(N)

print(arr[K])
print(result)