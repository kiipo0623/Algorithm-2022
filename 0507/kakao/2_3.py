from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

def bt(q1, q2, cnt):
    global answer
    print(q1, q2)
    if sum(q1) == sum(q2):
        answer = min(answer, cnt)
        return
    if len(q1)==0:
        return
    if len(q2)==0:
        return
    tmp_q1 = deepcopy(q1)
    tmp_q2 = deepcopy(q2)
    # q1에서 q2
    now = tmp_q1.popleft()
    tmp_q2.append(now)
    bt(tmp_q1, tmp_q2, cnt+1)
    #뒤처리
    tmp_q1.appendleft(now)
    tmp_q2.pop()
    # q2에서 q1
    now = tmp_q2.popleft()
    tmp_q1.append(now)
    bt(tmp_q1, tmp_q2, cnt+1)


def solution(queue1, queue2):
    global answer
    answer = int(1e9)
    SUM = sum(queue1) + sum(queue2)
    if SUM%2 == 1:
        return -1

    bt(deque(queue1), deque(queue2), 0)

    return answer
print(solution(
[3, 2, 7, 2], [4, 6, 5, 1]
))
# print(solution(
# [1, 2, 1, 2], [1, 10, 1, 2]
# ))
# print(solution(
# [1, 1], [1, 5]
# ))