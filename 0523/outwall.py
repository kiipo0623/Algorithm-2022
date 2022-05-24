cnt = int(1e9)
# visit : dict형태로 표시
def bt(friend_idx, visit):
    print()
    print(visit)
    global cnt, W, D, N
    if all(visit.values()): # 전부 방문 시
        cnt = min(cnt, friend_idx)
        return 0

    if friend_idx > cnt or friend_idx == len(D): # 더이상 볼 필요 X
        return 0

    leng = D[friend_idx]
    print("fidx: ", friend_idx)
    for idx, val in enumerate(W): # 방문 처리 : 해당 weak지점에서 출발
        if not visit[val]:
            start = val
            q = []
            for i in range(leng+1):
                pos = (i+start)%N
                print(pos)
                if visit.get(pos) == False:
                    visit[pos] = True
                    q.append(pos)
            bt(friend_idx+1, visit)
            for v in q:
                visit[v] = False


def solution(n, weak, dist):
    global cnt, W, D, N
    W, D, N = weak[:], sorted(dist, reverse=True)[:], n
    v = {i:False for i in weak}
    bt(0, v)
    if cnt == int(1e9):
        return -1
    else:
        return cnt

# print(solution(
#     12, [1,5,6,10],[1,2,3,4]
# ))
# print(solution(
# 12, [1, 3, 4, 9, 10], [3, 5, 7]
# ))
# print(solution(
# 200, [1, 11, 22, 33, 44, 55, 66, 80, 90, 100, 130, 160, 170, 181, 190], [1, 2, 3, 4, 5, 6, 7, 8]
# ))
print(solution(
    200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]
))