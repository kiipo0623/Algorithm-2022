# 앞에서부터 몇번째까지 합이 몇 되면 됨
# 넘어갔을 떄 

from collections import deque
def TFcheck(q):
    Flag = False
    for i in range(N-1):
        if q[i] != q[i+1] and not Flag:
            Flag = True
        elif q[i] != q[i+1] and Flag:
            return False
    return True

def check(visit):
    global N
    test = deque(list(visit.values()))
    for i in range(N):
        now = test.popleft()
        test.append(now)
        print(test)
        if TFcheck(test):
            return i+1
    return int(1e9)

# 중복 있으니까 dict으로
def bt(visited, nowsum, nowidx):
    global SOL, queue, visit_dict, answer
    if nowsum == SOL:
        print(visited)
        answer = min(answer, check(visited))
        return

    elif nowsum > SOL: # 실패
        return

    for idx in range(nowidx+1, len(queue)):
        if not visited[idx]:
            visited[idx] = True
            bt(visited, nowsum + queue[idx], nowidx + 1)
            visited[idx] = False

def solution(queue1, queue2):
    global SOL, queue, visit_dict, answer, N
    answer = int(1e9)
    queue = queue1+queue2
    N = len(queue)

    SUM = sum(queue)
    SOL = SUM//2

    if SUM%2 == 1:
        return -1
    if sum(queue1) == SOL:
        return 0

    # 합을 구하기 위한 백트래킹 진행
    visited = {idx:False for idx in range(len(queue))}
    # visit 인덱스 대응
    visit_dict = {}
    for i in range(len(queue)):
        visit_dict[i] = queue[i]

    bt(visited, 0, 0)
    if answer == int(1e9):
        return -1
    else:
        return answer

# print(solution(
# [3, 2, 7, 2], [4, 6, 5, 1]
# ))
print(solution(
[1, 2, 1, 2], [1, 10, 1, 2]
))
# print(solution(
# [1, 1], [1, 5]
# ))