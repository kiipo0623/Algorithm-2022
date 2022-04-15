# 삼성 기출 퇴사
import sys

input = sys.stdin.readline

N = int(input())
answer = [0] * (N+1)
T, P = [], []
for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

for i in range(N-1, -1, -1):
    if i+T[i]>N:
        answer[i] = answer[i+1]
    else:
        answer[i] = max(answer[i+1], P[i]+answer[T[i]+i])
print(answer[0])