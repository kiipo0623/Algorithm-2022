from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        now = q.popleft()
        if now == "123456789":
            return cntDict[now]

        pos = now.find("9")
        x = pos // 3
        y = pos % 3

        for i in range(4):
            nx =x + dx[i]
            ny = y+dy[i]

            if 0<= nx< 3 and 0<=ny<3:
                nPos = nx*3 + ny
                nextNum = list(now)
                nextNum[nPos], nextNum[pos] = nextNum[pos], nextNum[nPos]
                nextNum = ''.join(nextNum)

            if not cntDict.get(nextNum):
                q.append(nextNum)
                cntDict[nextNum] = cntDict[now] + 1

start = ''
for _ in range(3):
    temp = input().strip()
    temp = temp.replace(' ', '')
    start += temp

start = start.replace('0','9')

q = deque()
q.append(start)

cntDict = dict()
cntDict[start] = 0

result = bfs()
print(result if result != None else "-1")