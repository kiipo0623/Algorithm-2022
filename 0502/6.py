def checkout(row, col, R, C):
    if row<0 or row>=R or col<0 or col>=C:
        return True
    return False

def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    change = [[0] * M for _ in range(N)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = degree * (-1)
        change[r1][c1] += degree
        if not checkout(r1, c2+1, N, M):
            change[r1][c2+1] += degree*(-1)
        if not checkout(r2+1,c1, N, M):
            change[r2+1][c1] += degree*(-1)
        if not checkout(r2+1, c2+1, N, M):
            change[r2+1][c2+1] += degree

    for i in range(N):
        for j in range(M-1):
            change[i][j+1] += change[i][j]

    for i in range(N-1):
        for j in range(M):
            change[i+1][j] += change[i][j]

    for i in range(N):
        for j in range(M):
            board[i][j] += change[i][j]
            if board[i][j] > 0:
                answer += 1
    # print(board)

    return answer

# print(solution(
# [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
# [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# ))
print(solution(
[[1,2,3],[4,5,6],[7,8,9]],
[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
))