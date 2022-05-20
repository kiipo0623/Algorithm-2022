def solution(n, path, order):
    tree = [[] for _ in range(n)]
    for v1, v2 in path:
        tree[v1].append(v2)
        tree[v2].append(v1)

    orders = [0 for i in range(n)] #전에 가야하는 방 : 0은 어차피 가야하니까
    for pre, post in order:
        orders[post] = pre

    num_visit = 0
    after = {}

    visited = [False for i in range(n)]
    q = [0]

    while q:
        here = q.pop()
        # 방문하기 전에 들들러야하는 정점이 존재하면 체크
        if orders[here] and not visited[orders[here]]: # 이전 정점이 방문되었다면? 이미 내가 큐에 들어 있는 것
            after[orders[here]] = here # 방문은 했으니까 순서 조건 체크
            continue

        visited[here] = True
        num_visit += 1

        for there in tree[here]: # 방문 여부만 체크하고 추가 : 예외사항 미고려
            if not visited[there]:
                q.append(there)

        if here in after: # 지금 방문하는 곳이 after에 포함되어 있으면 이제 갈수있음
            q.append(after[here])

    return n == num_visit

print(solution(
    9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]
))

# 왜 orders를 갱신해주지 않는지