from collections import defaultdict, deque
from itertools import combinations

def solution(k, num, links):
    # 컷 할 edge 찾기 (완전탐색)
    # 해당 노드 기준으로 sum 구하기
    if k == 1:
        return sum(num)

    INF = int(1e9)
    answer = INF
    N = len(num)
    maxlen, root = -1, -1
    tree = defaultdict(list)

    for i in range(len(num)):
        q = deque([i])
        while q:
            now = q.popleft()
            for v in links[now]:
                if v != -1:
                    tree[i].append(v)
                    q.append(v)

        if maxlen<len(tree[i]):
            maxlen, root = len(tree[i]), i

    edges = [i for i in range(N) if i != root]

    candidate = list(combinations(edges, k-1))
    for c in candidate:
        group = []
        rootsum = sum(num)
        for edge in c:
            q = deque([edge])
            S = 0
            while q:
                now = q.popleft()
                S += num[now]
                for l in links[now]:
                    if l != -1 and l not in c:
                        q.append(l)
            rootsum -= S
            group.append(S)
        group.append(rootsum)
        answer = min(answer, max(group))


    return answer
#
# print(solution(
#     3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
# ))
print(solution(
    1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
))
# print(solution(
#     2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
# ))
# print(solution(
#     4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
# ))