N, M = map(int, input().split())
board = []
def solution():
    if N == M:
        garo, sero = 0, 0
        for i in range(N):
            garo += sum(int(board[i]))
            tmp = ''
            for j in range(N):
                tmp += board[j][i]
            sero += int(tmp)

for _ in range(N):
    board.append(input().rstrip())

