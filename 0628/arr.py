def check(sel):
    global Info, MAX_diff, best
    apeach, ryan = 0, 0
    # 승패계산
    for i in range(11):
        if Info[i] == sel[i] == 0:
            continue
        elif Info[i] >= sel[i]:
            apeach += (10 - i)
        elif Info[i] < sel[i]:
            ryan += (10 - i)
    print("ape", apeach, "ryan", ryan ,ryan-apeach, MAX_diff)
    if ryan <= apeach:
        return

    # 차이 계산
    if MAX_diff < (ryan - apeach):
        MAX_diff = (ryan - apeach)
        best = sel[:]
        print("update")
        return

    elif MAX_diff > (ryan - apeach):
        return

    elif MAX_diff == (ryan - apeach):
        for i in range(10, -1, -1):
            if sel[i] == best[i]:
                continue
            elif sel[i] > best[i]:
                best = sel[:]
                print("update")
                return
            elif sel[i] < best[i]:
                return


def backtrack(arrows, idx, select):
    global Info
    if idx == 11:
        tmp = select[:]
        if arrows:
            tmp[-1] += arrows
        print("arr", arrows, "idx", idx)
        print("sel", tmp)
        check(tmp)
        return

    backtrack(arrows, idx + 1, select)

    # 승리
    if arrows >= (Info[idx] + 1):
        tmp = (Info[idx] + 1)
        select[idx] += tmp
        backtrack(arrows - tmp, idx + 1, select)
        select[idx] -= tmp


def solution(n, info):
    global answer, Info, MAX_diff, best
    Info = info
    MAX_diff = 0
    best = [0] * 11
    backtrack(n, 0, best)
    if best == [0] * 11:
        return [-1]
    else:
        return best

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))