max_diff = -1
nice_ryan = []
def checksmall(r, a):
    for i in range(11, -1, -1):
        if r[i] > a[i]:
            return True
        elif r[i] < a[i]:
            return False

def bt(idx, rgrade, agrade, ryan, used, n, info):
    global max_diff, nice_ryan
    if idx == 11:
        if n-used>0:
            ryan[-1] += (n-used)
        if rgrade > agrade:
            if max_diff < rgrade-agrade:
                max_diff = rgrade-agrade
                nice_ryan = ryan[:]
            elif max_diff == (rgrade-agrade) and checksmall(ryan, nice_ryan):
                nice_ryan = ryan[:]
        return

    elif used == n:
        if n-used>0:
            ryan[-1] += (n-used)
        if rgrade > agrade:
            if max_diff < rgrade-agrade:
                max_diff = rgrade-agrade
                nice_ryan = ryan[:]
            elif max_diff == (rgrade-agrade) and checksmall(ryan, nice_ryan):
                nice_ryan = ryan[:]
        return

    # 패배 백트
    bt(idx+1, )




def solution(n, info):
    answer = []
    return answer