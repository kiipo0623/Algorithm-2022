import sys
from collections import deque

INF = int(sys.maxsize)
dp_min = [INF]*101

count = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# 사용개수, 값 / 0 제외
initial = [[value, idx] for idx, value in enumerate(count)][1:]
queue = deque(initial)

while queue:
    cnt, make = queue.popleft()
    dp_min[cnt] = min(dp_min[cnt], make)
    if dp_min[cnt] != make: # 원래거 그냥 쓰는 경우?
        continue
    for i in range(10):
        if cnt + count[i] <= 100:
            queue.append([cnt+count[i], int(str(make)+str(i))])

# TC = int(input())
#
# for _ in range(TC):
#     num = int(input())
