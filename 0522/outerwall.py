minn = int(1e9)
Dist, Weak = [], []
N = 0
def backtrack(friend_idx, weak_check, weak_idx):
    global minn, Dist, N
    if all(weak_check):
        minn = min(minn, friend_idx)
        return

    # 모든 경우의 수 다 고려
    if weak_idx == len(Weak):
        return

    # 볼 필요 없음 : 백트래킹
    if friend_idx >= minn:
        return

    # 모든 친구 소진
    if friend_idx == len(Dist):
        return

    start = Weak[weak_idx]
    if weak_check[start]: # 이미 방문했으면
        backtrack(friend_idx, weak_check, weak_idx+1)
    for idx in range(start, N):
        if not weak_check[idx]:
            change = []
            for cnt in range(Dist[friend_idx]+1):
                pos = (idx+cnt)%N
                if not weak_check[pos]:
                    change.append(pos)
                    weak_check[pos] = True

            backtrack(friend_idx+1, weak_check, weak_idx+1) # pos로 종료해야하는지?

            for c in change:
                weak_check[c] = False


def solution(n, weak, dist):
    global N, Dist, minn, Weak
    N = n
    Dist, Weak = sorted(dist, reverse=True)[:], weak[:]
    weak_chk = [True]*N

    for w in weak:
        weak_chk[w] = False

    backtrack(0, weak_chk, 0)

    if minn == int(1e9):
        return -1
    else:
        return minn

print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]	))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print(solution(200,
#                [1, 11, 22, 33, 44, 55, 66, 80, 90, 100, 130, 160, 170, 181, 190], [1, 2, 3, 4, 5, 6, 7, 8]
#                ))