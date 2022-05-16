def solution(n):
    answer = []
    board = [[0] * n for _ in range(n)]
    idx, num = 0, 0
    row, col = -1, 0
    for i in range(n, 0, -1):

        if idx % 3 == 0:
            for _ in range(i):
                row += 1
                num += 1
                board[row][col] = num

        elif idx % 3 == 1:
            for _ in range(i):
                col += 1
                num += 1
                board[row][col] = num

        elif idx % 3 == 2:
            for _ in range(i):
                col -= 1
                row -= 1
                num += 1
                board[row][col] = num

        idx += 1

    for b in board:
        for a in b:
            if a != 0:
                answer.append(a)

    return answer

print(solution(5))