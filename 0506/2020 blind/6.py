# weakvisit : dict 전체 써서 / friend : deque써서 pop하는 식으로
from collections import deque
from copy import deepcopy
def bt(weak, friend, friend_leng, n):
    global answer
    print(weak, friend)
    if len(weak) == 0:
        answer = min(answer, friend_leng - len(friend))
        return
    if len(friend) == 0:
        return

    tmpfriend = deepcopy(friend)
    nowfriend = tmpfriend.popleft()
    for w in weak:
        tmpweak = deepcopy(weak)
        for idx in range(nowfriend+1):
            if (w+idx)%n in weak:
                tmpweak.remove((w+idx)%n)
        bt(tmpweak, tmpfriend, friend_leng, n)

        tmpweak = deepcopy(weak)
        for idx in range(nowfriend+1):
            if (w - idx) % n in weak:
                tmpweak.remove((w - idx) % n)
        bt(tmpweak, tmpfriend, friend_leng, n)
    tmpfriend.appendleft(nowfriend)

def solution(n, weak, dist):
    global answer
    answer = len(dist)+1
    dist.sort(reverse=True)
    weak = deque(weak)
    dist = deque(dist)
    bt(weak, dist, len(dist), n)
    if answer == len(dist)+1:
        return -1
    else:
        return answer

# print(solution(
#     12, [1, 5, 6, 10], [1, 2, 3, 4]
# ))
print(solution(
    12, [1, 3, 4, 9, 10], [3, 5, 7]
))
# print(solution(
# 200, [1, 11, 22, 33, 44, 55, 66, 80, 90, 100, 130, 160, 170, 181, 190], [1, 2, 3, 4, 5, 6, 7, 8]
# ))