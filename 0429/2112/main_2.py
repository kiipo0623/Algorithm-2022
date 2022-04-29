from copy import deepcopy
def check(b):
    for w in range(W):
        cnt, flag, before = 1, False, b[0][w]
        for d in range(1, D):
            if before == b[d][w]:
                cnt += 1
            else:
                cnt, before = 1, b[d][w]

            if cnt>=K:
                flag = True
        if not flag:
            return False
    return True

def bt(cnt,b, updated):
    global answer
    if cnt>=answer:
        return

    if check(b):
        answer = min(answer, cnt)
        return

    start = lst.index(updated[-1][0])+1 if updated else 0
    for i in range(start, D):
        before = [t[:] for t in b]
        # A로 갱신
        for w in range(W):
            b[i][w] = 0
        updated.append((i, 0))
        bt(cnt+1, b, updated)
        b = [t[:] for t in before]
        updated.pop()

        # B로 갱신
        for w in range(W):
            b[i][w] = 1
        updated.append((i, 1))
        bt(cnt+1, b, updated)
        b = [t[:] for t in before]
        updated.pop()

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())
for t in range(1,T+1):
    D, W, K = map(int, input().split())
    board = []
    answer = int(1e9)
    lst = [i for i in range(D)]
    for _ in range(D):
        board.append(list(map(int, input().split())))
    bt(0, board, [])
    print("#%d %d"%(t, answer))
