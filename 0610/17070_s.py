import sys
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
result = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
# dir row col
result[0][0][1] = 1

# 맨처음에 가로로 되어있으니깐
for i in range(2, n):
    if s[0][i] == 0:
        result[0][0][i] = result[0][0][i-1]

for i in range(1, n):
    for j in range(2, n):
        if s[i][j] == 0 and s[i-1][j] == 0 and s[i][j-1] == 0:
            result[2][i][j] = result[0][i-1][j-1] + result[1][i-1][j-1] + result[2][i-1][j-1]

        if s[i][j] == 0:
            result[0][i][j] = result[0][i][j-1] + result[2][i][j-1]
            result[1][i][j] = result[1][i-1][j] + result[2][i-1][j]

print(result[0][n-1][n-1] + result[1][n-1][n-1] + result[2][n-1][n-1])