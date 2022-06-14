from collections import deque

S = int(input())
q = deque()
q.append([1, 0, 0])
visited = [[0 for _ in range(2001)] for _ in range(2001)]

while q:
    screen, clip, time = q.popleft()
    if screen == S:
        print(time)
        break

    if screen > 2000 or clip > 2000 or visited[screen][clip]:
        continue
    visited[screen][clip] = 1

    q.append([screen, screen, time+1])
    if clip:
        q.append([screen+clip, clip, time+1])
    if screen > 0:
        q.append([screen-1, clip, time+1])