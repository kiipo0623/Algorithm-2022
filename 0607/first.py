# 행 : 선수 번호
# 열 : 포지션 번호
# 능력치 합의 최댓값 한 줄에 하나씩 출력
# 0이면 부적합, 양수이면 배치
def bt(idx, summ, selected):
    global board, answer
    if idx == 11:
        answer = max(answer, summ)
        return

    for i in range(11):
        if board[idx][i] != 0 and i not in selected:
            selected.append(i)
            bt(idx+1, summ+board[idx][i], selected)
            selected.pop()


import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    board = []
    answer = 0
    for i in range(11):
        board.append(list(map(int, input().split())))
    # 다 받은 다음에 백트래킹 진행
    bt(0, 0, [])
    print(answer)