from collections import defaultdict, deque
from itertools import permutations, product
INF = int(1e9)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

Board = []
# distance 는 어차피 모든 보드를 다 갱신해야 하기 때문에 도착지와 무관하다

# 카드 번호 자체 순서, 두 카드중 뭘 먼저 할지, 완전 시작 커서
def simulate(outer_order, inner_order, r, c):
    global Board
    cost = 0
    now_r, now_c = r, c

    for idx, cardnum in enumerate(outer_order):
        for AB in inner_order[idx]:
            next_r, next_c = card[cardnum][AB]
            print("next ", next_r, next_c)

            q = deque()
            q.append((0, now_r, now_c))
            dist = [[INF] * 4 for _ in range(4)]
            dist[now_r][now_c] = 0

            while q:
                cost, nr, nc = q.popleft()
                # 범위 안에 포함되고, 원래 값 이하이면 (방문 가치가 있으면)/ 다익스트라로 하는거 ??
                if 0 <= nr < 4 and 0 <= nc < 4 and dist[nr][nc] >= cost:
                    dist[nr][nc] = cost
                    for k in range(4):
                        # 한칸만 가는거
                        # 끝까지 가는거 : 마지막 칸에 해당하거나 새로운 카드가 나올 떄까지 : 최대 4칸까지 가능
                        dr, dc = nr, nc
                        while True:
                            dr, dc = dr + dx[k], dc + dy[k]
                            if not 0<=dr<4 or not 0<=dc<4:
                                dr -= dx[k]
                                dc -= dy[k]
                                break
                            elif Board[dr][dc]:
                                break
                        q.append((cost+1, dr, dc))
                        if 0 <= nr+dx[k] < 4 and 0 <=nc+dy[k] < 4:
                            q.append((cost+1, nr+dx[k], nc+dx[k]))

            print("dist ", dist)
            # 커서 위치 업뎃 하기
            cost += dist[next_r][next_c]
            now_r, now_c = next_r, next_c


    print("last cost ", cost)
    return cost


    print(dist)
    print(cost)

    print("outer ", outer_order)
    print("inner ", inner_order)
    return


def solution(board, r, c):
    global card, Board
    Board = [a[:] for a in board]
    answer = int(1e9)
    card = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card[board[i][j]].append((i, j))

    # 외부 순서 설정 / 내부 순서 설정 : [(0, 1), (1, 0), (0, 1)]
    outer = list(permutations(card.keys()))
    inner = list(product([[0, 1], [1, 0]], repeat=len(card)))
    print(inner)

    for o in outer:
        for i in inner:
            answer = min(answer, simulate(o, i, r, c))


    return answer

print(solution(
[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0
))