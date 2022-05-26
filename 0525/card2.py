from collections import defaultdict, deque
from itertools import permutations, product
INF = int(1e9)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

# distance 는 어차피 모든 보드를 다 갱신해야 하기 때문에 도착지와 무관하다
def get_dist(r, c, b, dest_r, dest_c):
    # 현재 보드 상태에 대해서 전체 거리탐
    queue = deque()
    queue.append((0, r, c))
    dist = [[INF]*4 for _ in range(4)]

    while queue:
        cost, row, col = queue.popleft()
        if dist[row][col] > cost:
            dist[row][col] = cost

            for k in range(4):
                # 거리가 최대인 것 : 가까운 것부터 탐색하게 됨
                # 세 가지 경우 : 정상/끝까지/내가끝
                for i in range(1, 4):
                    new_r, new_c = row+dx[k]*i, col+dy[k]*i
                    # 벗어나는 경우 : 이전으로 돌아와서 끝냄
                    if new_r<0 or new_r>=4 or new_c<0 or new_c>=4:
                        new_r -= dx[k]
                        new_c -= dy[k]
                        break
                    # 값이 있는 경우 : 그냥 끝냄
                    if b[new_r][new_c]:
                        break
                # if dist[new_r][new_c] > cost+1:
                queue.append((cost+1, new_r, new_c))

                # 거리가 1인 것
                if 0<=row+dx[k]<4 and 0<=col+dy[k]<4:
                        # and dist[row+dx[k]][col+dy[k]] > cost+1:
                    queue.append((cost+1, row+dx[k], col+dy[k]))
    print("TO ", dest_r, dest_c, "cost ", dist[dest_r][dest_c])
    print("dist")
    print(dist)

    return dist[dest_r][dest_c]


# 카드 번호 자체 순서, 두 카드중 뭘 먼저 할지, 완전 시작 커서
def simulate(outer_order, inner_order, r, c, board):
    b = [a[:] for a in board]
    now_r, now_c = r, c
    cost = 0
    for idx, cardnum in enumerate(outer_order):
        for AB in inner_order[idx]:
            next_r, next_c = card[cardnum][AB]
            cost += get_dist(now_r, now_c, b, next_r, next_c)
            b[next_r][next_c] = 0
            now_r, now_c = next_r, next_c
    print("outer ", outer_order)
    print("inner ", inner_order)
    print("cost ", cost)
    print()
    return cost


def solution(board, r, c):
    global card
    answer = int(1e9)
    card = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card[board[i][j]].append((i, j))
    print(card)

    outer = list(permutations(card.keys()))
    inner = list(product([[0, 1], [1, 0]], repeat=len(card)))

    for o in outer:
        for i in inner:
            answer = min(answer, simulate(o, i, r, c, board))


    return answer + len(card)*2

print(solution(
[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0
))
print(solution(
[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1
))
