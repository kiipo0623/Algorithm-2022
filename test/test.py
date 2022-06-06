from collections import defaultdict, deque
from copy import deepcopy

is_wolf = list()
num2edges = defaultdict(list)
max_sheep = 0

def find_max_recursive(current_loc, used, nsheep, nwolf, can_go):
    global max_sheep
    if used[current_loc]: # 현재 노드를 방문한 경우
        return

    used[current_loc] = True # 방문 기록
    if is_wolf[current_loc]: # 늑대인 경우
        nwolf += 1
    else:
        nsheep += 1
        max_sheep = max(max_sheep, nsheep)

    if nsheep <= nwolf:
        return

    can_go.extend(num2edges[current_loc])
    for next_loc in can_go:


def solution(info, edges):
    global is_wolf, num2edges, max_sheep
    is_wolf = info

    for e_from, e_to in edges:
        num2edges[e_from].append(e_to)

    find_max_recursive(0, used, 0, 0, [])
    return max_sheep