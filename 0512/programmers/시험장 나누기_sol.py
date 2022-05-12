import sys
sys.setrecursionlimit(10**6)

l = [0]*10005 # 왼쪽 자식
r = [0]*10005 # 오른쪽 자식
x = [0]*10005 # 응시 인원
p = [-1]*10005 # 부모 노드 번호
n = 0 # 노드의 수
root = 0

cnt = 0 # 그룹의 수

# 현재 노드 번호, 최대 인원
def dfs(cur, lim):
    global cnt
    lv = 0
    if l[cur] != -1:
        lv = dfs(l[cur], lim)
    if r[cur] != -1:
        rv = dfs(r[cur], lim)
    #왼쪽 오른쪽 모두 합해도 lim 이하
    if x[cur] + lv + rv <= lim:
        return x[cur]+lv+rv
    # 왼쪽 오른쪽 중 작은 것 lim 이하
    if x[cur] + min(lv, rv) <= lim:
        cnt += 1
        return x[cur] + min(lv, rv)
    if x[cur] + min(lv, rv):
        cnt += 2
        return x[cur]

def solve(lim):
    global cnt
    cnt = 0
    dfs(root, lim)
    cnt += 1 # 마지막으로 남은 인원 그룹
    return cnt

def solution(k, num, links):
    global root
    n = len(num)
    for i in range(n):
        l[i], r[i] = links[i]
        x[i] = num[i]
        if l[i] != -1: p[l[i]] = i
        if r[i] != -1: p[r[i]] = i

    for i in range(n):
        if p[i] == -1:
            root = i
            break

    start = max(x) # 한 그룹에 포함되는 최소 수
    end = 10 ** 8 # 한 그룹에 포함되는 최대 수
    while start < end:
        mid = (start+end)//2
        if solve(mid) <= k: # 성공했고 최소를 찾아야
            end = mid
        else:
            start = mid + 1
    return start