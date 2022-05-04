from collections import defaultdict, deque
from itertools import combinations

# 양쪽을 자르는 경우를 안 쳐서 에러 ~
def solution(k, num, links):
    if k == 1:
        return sum(list)

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
    print(tree)

    sumlist = [num[i] for i in range(N)]

    for leng in range(maxlen+1): # 자식 수가 작은 것부터
        for idx in range(N):
            if len(tree[idx]) == leng:
                for item in links[idx]:
                    if item != -1:
                        sumlist[idx] += sumlist[item]

    edges = [i for i in range(N) if i != root]
    candidate = list(map(list, combinations(edges, k-1)))

    for c in candidate:
        group = []
        # root는 전체 sum에서 역대 제외한 것 빼면
        for idx in c:  # idx 자기 위에 있는 간선
            tmp = sumlist[idx]
            for s in tree[idx]:
                if s in c:
                    tmp -= sumlist[s]
                    break
            group.append(tmp)
        rootstart = sumlist[root] - sum(group)
        group.append(rootstart)
        answer = min(answer, max(group))
    return answer



print(solution(
    3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
))
# print(solution(
#     1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]
# ))