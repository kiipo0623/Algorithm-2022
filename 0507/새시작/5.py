from collections import deque
def solution(rc, operations):
    answer = [[]]
    for operation in operations:
        tmp = [a[:] for a in rc]
        if operation == "ShiftRow":
            tmp = deque(tmp)
            tmp.rotate(1)
            rc = [a[:] for a in tmp]
        elif operation == "Rotate":
            N, M = len(rc), len(rc[0])
            res = tmp[0][0]
            for k in range(0, N-1):
                before = tmp[k+1][0]
                tmp[k][0] = before

            for k in range(0, M-1):
                before = tmp[N-1][k+1]
                tmp[N-1][k] = before

            for k in range(N-1, -1, -1):
                before = tmp[k-1][M-1]
                tmp[k][M-1] = before

            for k in range(M-1, 0, -1):
                before = tmp[0][k-1]
                tmp[0][k] = before

            tmp[0][1] = res
            rc = [a[:] for a in tmp]

    return rc

print(solution(
[[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate"]
))