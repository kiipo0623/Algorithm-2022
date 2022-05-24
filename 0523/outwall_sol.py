from itertools import permutations
from collections import deque
CNT = int(1e9)
def simulation(weak, frd, dist):
    global CNT
    for i in range(len(weak)):
        weak = weak[i:] + weak[:i]
        w = deque(weak)
        print(w)
        cnt = 0
        for f in frd:
            if len(w) == 0:
                break
            cnt += 1
            start = w.popleft()
            end = start + dist[f]
            while w:
                if w[0] <= end:
                    w.popleft()
                else:
                    break
        print(cnt)
        CNT = min(CNT, cnt)

def solution(n, weak, dist):
    global CNT
    friend_turn = list(permutations(range(len(dist)), len(dist)))
    for frd in friend_turn:
        simulation(weak, frd, dist)
    if CNT == int(1e9):
        return -1
    else:
        return CNT

# print(solution(
#     12, [1,5,6,10],[1,2,3,4]
# ))
# print(solution(
# 12, [1, 3, 4, 9, 10], [3, 5, 7]
# ))
# print(solution(
# 200, [1, 11, 22, 33, 44, 55, 66, 80, 90, 100, 130, 160, 170, 181, 190], [1, 2, 3, 4, 5, 6, 7, 8]
# ))
# print(solution(
#     200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]
# ))