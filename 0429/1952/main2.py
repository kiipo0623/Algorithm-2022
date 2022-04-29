def bt(last):
    global answer
    if last == 12:
        return

    # 한달 추가 : 무조건 있을 수밖에
    dp[last+1] = min(dp[last+1], dp[last] + min(money[0]*plan[last+1], money[1]))
    bt(last+1)

    # 세달 추가
    next= min(last+3, 12)
    dp[next] = min(dp[next], dp[last] + money[2])
    bt(next)

    next = min(last+12, 12)
    dp[next] = min(dp[next], dp[last]+money[3])

import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for t in range(1, T+1):
    money = list(map(int, input().split())) # 1일 1달 3달 1년
    plan = [0] + list(map(int, input().split()))
    answer = int(1e9)
    INF = int(1e9)
    dp = [INF]*13
    dp[0] = 0
    bt(0)
    print("#{} {}".format(t, dp[-1]))
    print(dp)
    print()