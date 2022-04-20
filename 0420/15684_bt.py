def check():
    for i in range(1, n+1): # 각 세로줄에 대해서
        temp = i # 가로 인덱스
        for j in range(1, h+1):
            if s[j][temp] == 1:
                temp += 1
            elif s[j][temp-1] == 1:
                temp -= 1
        if temp != i:
            return False
    return True

def dfs(num, cnt):
    global result
    if result != 5:
        return
    if num == cnt:
        if check():
            result = cnt
        return
    for j in range(1, n):
        for i in range(1, h+1):
            if s[i][j-1] == 0 and s[i][j+1] == 0 and s[i][j] == 0:
                s[i][j] = 1
                dfs(num, cnt+1)
                s[i][j] = 0

                while i<h: # 이부분이 뭐하는건지 ?
                    if s[i][j-1] or s[i][j+1]: # 양쪽에 있으면 i를 1키우라는 뜻 어차피 그 라인에는 못그리니까[연속]
                        break
                    i += 1

inf = 5
n, m, h = map(int, input().split())
s = [[0]*(n+1) for i in range(h+1)]
result = inf

for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1

for i in range(4):
    dfs(i, 0)
    if result != inf:
        print(result)
        break
if result == inf:
    print(-1)