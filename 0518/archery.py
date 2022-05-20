# 백트래킹
Info = []
best, bestgrade = [0]*11, -1
def gradecount(ryan):
    global Info
    a, r = 0, 0
    for i in range(11):
        if Info[i] == 0 and ryan[i] == 0:
            continue
        elif Info[i] >= ryan[i]:
            a += (10-i)
        elif Info[i] < ryan[i]:
            r += (10-i)
    if a >= r: # 구태여 할 필요 없음 더 작으면 값이 음수가 되니까
        return -1
    else:
        return (r-a)

def best_choice(ryan, res): # 0번째부터 값을 추가하면 뒤에 다 들어가기 때문에 굳이 할 필요 없음
    global bestgrade, best
    if ryan > bestgrade:
        bestgrade, best = ryan, res[:]
    elif ryan == bestgrade:
        for i in range(10, -1, -1):
            if best[i] < res[i]:
                best = res[:]
                return
            elif best[i] > res[i]:
                return


def backtracking(arrow, res, now):
    global Info
    tmp = res[:]
    if now == 11: # 모든 점수 다 봤음
        if arrow > 0:
            tmp[-1] += arrow
        grade = gradecount(tmp)
        if grade > 0:
            best_choice(grade, tmp)
        return

    if arrow == 0:
        grade = gradecount(tmp)
        if grade > 0:
            best_choice(grade, tmp)
        return

    tmp = res[:]
    if Info[now]+1 <= arrow:
        tmp[now] = Info[now]+1
        backtracking(arrow-(Info[now]+1), tmp, now+1)
        tmp[now] = 0
    backtracking(arrow, res, now+1)



def solution(n, info):
    global bestgrade, best, Info
    answer = [-1]
    Info = info[:]
    backtracking(n, [0]*11, 0)

    if bestgrade > 0:
        return best
    else:
        return answer

print(solution(
    # 5, [2,1,1,1,0,0,0,0,0,0,0]
    # 1, [1,0,0,0,0,0,0,0,0,0,0]
    9, [0,0,1,2,0,1,1,1,1,1,1]
))
