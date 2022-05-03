def winchecker(ryan, info):
    apeachgrade, ryangrade = 0, 0
    for i in range(11):
        if info[i] >= ryan[i] and info[i] != 0:
            apeachgrade += (10-i)
        elif info[i]<ryan[i]:
            ryangrade += (10-i)
    if ryangrade > apeachgrade:
        return [True, ryangrade-apeachgrade]
    else:
        return [False, -1]

def checksmall(new, old):
    for i in range(10, -1, -1):
        if new[i] > old[i]:
            return new[:]
        elif new[i] < old[i]:
            return old[:]
    return new[:]

def bt(idx, ryan, usecnt, n, info):
    global max_diff, max_ryan
    if idx == 11:
        if usecnt<n:
            ryan[-1] += n - sum(ryan)
        res = winchecker(ryan, info)
        if res[0]: #일단 이겼고
            if res[1] > max_diff: # 점수차 더크면 무조건 갱신
                max_diff = res[1]
                max_ryan = ryan[:]
            elif res[1] == max_diff:
                max_ryan = checksmall(ryan, max_ryan)[:]
        return

    if usecnt == n:
        # candidate.add(ryan)끝
        res = winchecker(ryan, info)
        if res[0]:  # 일단 이겼고
            if res[1] > max_diff:  # 점수차 더크면 무조건 갱신
                max_diff = res[1]
                max_ryan = ryan[:]
            elif res[1] == max_diff:
                max_ryan = checksmall(ryan, max_ryan)[:]
        return

    # 실패 백트
    bt(idx + 1, ryan, usecnt, n, info)

    # 승리하는 경우 백트래킹
    if info[idx]+1+usecnt <= n:
        ryan[idx] = info[idx]+1
        bt(idx+1, ryan, usecnt+info[idx]+1, n, info)
        ryan[idx] = 0

max_diff = -1
max_ryan = []

def solution(n, info):
    global max_diff, max_ryan
    bt(0, [0]*11, 0, n, info)
    if max_diff == -1:
        return [-1]
    else:
        return max_ryan[:]

