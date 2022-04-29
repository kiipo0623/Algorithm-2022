def checker(b):
    for i in range(W):
        cnt, before = 1, b[0][i]
        for j in range(1, D):
            if before == b[j][i]:
                cnt += 1
            else:
                cnt, before = 1, b[j][i]
        if cnt<K:
            return False
    return True

def bt(b, medicine, cnt):
    if checker(b):
        return cnt



T = int(input())
for _ in range(1,T+1):
    D, W, K = map(int, input().split())
    board = []
    for _ in range(D):
        board.append(list(map(int, input().split())))
        bt()