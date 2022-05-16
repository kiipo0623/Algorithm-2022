from collections import defaultdict

N = int(input())
num = list(map(int, input().split()))
dp = [dict() for _ in range(N)]
dp[0][num[0]] = 1

for idx, val in enumerate(num):  # 1번부터 진행, 마지막은 등호만 넣으면 돼서 미진행
    if idx == 0 or idx >= N-1:
        continue

    for item in dp[idx - 1].keys():
        if 0<=item + val <= 20:
            if item + val in dp[idx]:
                dp[idx][item + val] += dp[idx - 1][item]
            else:
                dp[idx][item + val] = dp[idx - 1][item]

        if 0 <= item - val <= 20:
            if item - val in dp[idx]:
                dp[idx][item - val] += dp[idx - 1][item]
            else:
                dp[idx][item - val] = dp[idx - 1][item]

answer = 0
for key, val in dp[N-2].items():
    if key == num[N-1]:
        answer += val
print(answer)