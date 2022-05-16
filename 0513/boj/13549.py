from collections import deque
INF = float('inf')
visited = [INF]*100001
def bfs(start):
    global visited
    queue = deque()
    queue.append((start, 0))
    visited[start] = 0

    while queue:
        now_pos, cnt = queue.popleft()
        print(now_pos, cnt)

        # 3가지 이동
        if 0<=now_pos+1<=100000 and visited[now_pos+1] > cnt+1:
            visited[now_pos+1] = cnt+1
            queue.append((now_pos+1, cnt+1))

        if 0<=now_pos-1<=100000 and visited[now_pos-1] > cnt+1:
            visited[now_pos-1] = cnt+1
            queue.append((now_pos-1, cnt+1))

        if 0<=now_pos*2<=100000 and visited[now_pos*2] > cnt:
            visited[now_pos*2] = cnt
            queue.append((now_pos*2, cnt))

N, K = map(int, input().split())
bfs(N)
print(visited[K])
