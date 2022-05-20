#-*- coding: utf-8 -*-

from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

link_dict = defaultdict(list)
need_dict = defaultdict(list)

def solution(n, path, order):
    for a, b in path:
        link_dict[a].append(b)
        link_dict[b].append(a)

    set_need_dict(0, -1)

    for a, b in order:
        need_dict[b].append(a)

    visited = [False for _ in range(n)]
    recur = [False for _ in range(n)]
    for i in range(n):
        if is_cycle(i, visited, recur):
            return False
    return True

def set_need_dict(node, parent_node):
    for next_node in link_dict[node]:
        if next_node == parent_node: # 부모 노드면 패스
            continue
        need_dict[next_node].append(node)
        set_need_dict(next_node, node)

def is_cycle(node, visited, recur):
    if visited[node]:
        return True
    if recur[node]:
        return False

    visited[node] = True #방문 체크
    recur[node] = True # 이 하 노드 사이클 존재 여부 확인 체크 : True상태로 내버려둔다

    for parent_node in need_dict[node]:
        if is_cycle(parent_node, visited, recur):
            return True
    visited[node] = False # 리프 노드까지 갔을 때
    return False

print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]
))