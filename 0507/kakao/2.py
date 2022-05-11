from collections import deque
def simulate(visit):

# 중복 있으니까 dict으로
def bt(visited, nowsum, nowidx):
    global SOL, queue, visit_dict
    if nowsum == SOL:
        change = 0
        for idx in range(len(visited)-1):
            if visited[idx] != visited[idx+1]:
                change+=1
            if change>2:
                break
        if change<=2:
            simulate(visited)
        return

    elif nowsum > SOL: # 실패
        return

    for idx in range(nowidx+1, len(queue)):
        if not visited[idx]:
            visited[idx] = True
            bt(visited, nowsum + queue[idx], nowidx + 1)
            visited[idx] = False

def solution(queue1, queue2):
    global SOL, queue, visit_dict, answer
    answer = int(1e9)
    queue = queue1+queue2

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

print(solution(
[3, 2, 7, 2], [4, 6, 5, 1]
))