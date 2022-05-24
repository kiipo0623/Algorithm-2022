count = 0

def backtracking(line, b, n):
    global count
    if line == n:
        print(b)
        count += 1
        return

    for i in range(0, n): # 가로 어디에 놓을지
        flag = True
        for j in range(line): # 0부터 이전 줄까지
            if b[j] == i:
                break
            if abs(b[j]-i) == (line-j):
                break
        else:
            b[line] = i
            backtracking(line+1, b, n)
            b[line] = 0


def solution(n):
    global count
    board = [0]*n
    backtracking(0, board, n)
    return count

print(solution(10))