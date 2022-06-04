Board = []
stack = []
answer = 0

def getdoll(move):  # 구하기만 함
    global Board, N, stack, answer
    for i in range(N):
        if Board[i][move] != 0:  # 인형 있으면
            num = Board[i][move]
            Board[i][move] = 0
            print("num", num)
            print(stack)
            if stack and stack[-1] == num:
                answer += 2
                stack.pop()
            else:
                stack.append(num)
            break


def solution(board, moves):
    global Board, N, stack, answer
    N = len(board)
    Board = [a[:] for a in board]
    for move in moves:
        getdoll(move - 1)

    return answer

print(solution(
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
[1,5,3,5,1,2,1,4]
))