N, M = map(int, input().split())
tree = list(map(int, input().split()))

# 최댓값을 구하고자 함
def treecut(H): # 얻은 나무 반환
    s = 0
    for t in tree:
        if t>H:
            s += (t-H)
    return s

start, end = 0, 1000000000
while start < end:
    mid = (start + end)//2
    if treecut(mid) > M: # 이것도 된다는 뜻
        start = mid+1
    elif treecut(mid) == M:
        start = mid+1
    elif treecut(mid) < M:
        end = mid
print(mid)