import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

tree = dict() # 자식노드
idx_node = dict() # 좌표

pre = []
post = []

def find_tree(depthidx, nodeidx, Lstart, Rend):
    global tree, level, N, idx_node, depthnode
    if depthidx == len(level)-1:
        tree[nodeidx] = [-1, -1]
        return

    tmp = [-1, -1]
    mid = idx_node[nodeidx][0]

    print("nodeidx = ", nodeidx, "Lstart = ", Lstart, "Rend = ", Rend, "mid", mid)
    for x, y, idx in depthnode[level[depthidx+1]]:
        if Lstart < x < mid:
            tmp[0] = idx
        elif mid < x < Rend:
            tmp[1] = idx
    tree[nodeidx] = tmp

    # 왼쪽 자식
    if tmp[0] != -1:
        find_tree(depthidx+1, tmp[0], Lstart, mid)
    if tmp[1] != -1:
        find_tree(depthidx+1, tmp[1], mid, Rend)

def pre_order(start):
    pre.append(start)
    if tree[start][0] != -1:
        pre_order(tree[start][0])
    if tree[start][1] != -1:
        pre_order(tree[start][1])

def post_order(start):
    if tree[start][0] != -1:
        post_order(tree[start][0])
    if tree[start][1] != -1:
        post_order(tree[start][1])
    post.append(start)


def solution(nodeinfo):
    global level, idx_node, depthnode
    answer = []

    level = set()
    depthnode = defaultdict(list)
    rootlevel = -1

    for idx, node in enumerate(nodeinfo):
        x, y = node
        level.add(y)
        idx_node[idx+1] = [x, y]
        depthnode[y].append([x, y, idx+1])
        if y>rootlevel: rootlevel = y

    rootidx = depthnode[rootlevel][0][2]
    level = sorted(list(level), reverse=True)
    find_tree(-1, rootidx, 0, 100001)

    pre_order(rootidx)
    post_order(rootidx)

    answer.append(pre)
    answer.append(post)
    return answer

print(solution(
[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
))