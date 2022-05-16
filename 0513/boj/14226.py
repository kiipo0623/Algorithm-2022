from collections import deque
S = int(input())
INF = float('inf')
visited = [[INF] *(1001) for _ in range(1001)]


def bfs():
    queue = deque()
    queue.append((1, 0, 0))
    while queue:
        display, clipboard, cnt = queue.popleft()

        # 복사
        if visited[display][display] > cnt+1:
            visited[display][display] = cnt+1
            queue.append((display, display, cnt+1))

        # 붙여넣기
        if display+clipboard <= 1000 and visited[display+clipboard][clipboard] > cnt+1:
            visited[display+clipboard][clipboard] = cnt+1
            queue.append((display+clipboard, clipboard, cnt+1))

        # 삭제
        if display-1 >= 0 and visited[display-1][clipboard] > cnt+1:
            visited[display-1][clipboard] = cnt+1
            queue.append((display-1, clipboard, cnt+1))

bfs()
print(min(visited[S]))