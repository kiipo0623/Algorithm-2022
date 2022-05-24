Weak, Dist = [], []
N = 0
minn = int(1e9)
# 친구 불러와서 빈 weak부터 탐색
def backtrack(weak, friend_idx):
    global Weak, Dist, N, minn
    print(weak)
    print(friend_idx)
    print()
    if len(weak) == 0:
        minn = min(minn, friend_idx)
        return

    if friend_idx == len(Dist):
        return

    if friend_idx >= minn:
        return

    for idx, w in enumerate(weak): # 현재 상황에 남아있는 weak에 대해서
        tmp = weak[:]
        start = weak[idx]
        for i in range(Dist[friend_idx]+1):
            pos = (start+i)%N
            if pos in tmp:
                tmp.remove(pos)
        backtrack(tmp, friend_idx+1)

def solution(n, weak, dist):
    global N, Weak, Dist
    answer = 0
    N, Weak, Dist = n, weak[:], sorted(dist, reverse=True)[:]
    t = weak[:]
    backtrack(t, 0)

    if minn == int(1e9):
        return -1
    else:
        return minn


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]	))
# print()
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
# print()
# print(solution(200,
#                [1, 11, 22, 33, 44, 55, 66, 80, 90, 100, 130, 160, 170, 181, 190], [1, 2, 3, 4, 5, 6, 7, 8]
#                ))
print(solution(
    200, [0, 100], [1,1]
))