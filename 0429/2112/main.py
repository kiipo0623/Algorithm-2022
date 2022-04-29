def checker(b):
    for i in range(W):
        cnt, before, flag = 0, b[0][i], False
        for j in range(1, D):
            if before == b[j][i]:
                cnt += 1
            else:
                cnt, before = b[j][i]
            if cnt>=K:
                flag = True
                break
        if not flag:
            return False
    return True

def update(before, idx, AB):
    for d in range(W):



def simulate():
    for cnt in range(D): # 몇개 약품처리 하는지
        for before in dp[cnt]: # 이전 개수에서 가져와서
            for i in range(D): # 앞에서부터 순서대로 처리
                if before[i] == 'X':
                    # 그 자리에 A, B 두가지에 대해서 표시한 뒤 체크
                    update(before, i, 0)

T = int(input())
for t in range(1,T+1):
    D, W, K = map(int, input().split())
    board = []
    dp = [[] for _ in range(D)]
    print(dp)
    for _ in range(D):
        board.append(list(map(int, input().split())))
    if checker(board):
        print("#%d %d"%(t, 0))
    else:
        simulate()