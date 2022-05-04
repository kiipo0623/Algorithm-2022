from collections import deque
def solution(n, k, cmd):
    answer = ''
    linkedlist = []
    OX = ['O']*n

    for i in range(n):
        tmp = [i-1, i, i+1]
        linkedlist.append(tmp)

    # 맨 마지막 next 없도록 지정
    linkedlist[-1][2] = -1
    # 현재 인덱스
    nowidx = k
    # 삭제
    stack = deque([])

    for c in cmd:
        if c[0] == 'U':
            cnt = int(c[2:])
            for _ in range(cnt):
                nowidx = linkedlist[nowidx][0]

        elif c[0] == 'D':
            cnt = int(c[2:])
            for _ in range(cnt):
                nowidx = linkedlist[nowidx][2]

        elif c[0] == 'C':
            before = linkedlist[nowidx][0]
            after = linkedlist[nowidx][2]
            stack.append(linkedlist[nowidx][1])
            OX[nowidx] = 'X'

            # 만약 첫번째 행이면
            if before == -1:
                linkedlist[after][0] = before
                nowidx = after
            # 만약 마지막 행이면
            elif after == -1:
                linkedlist[before][2] = after
                nowidx = before
            # 아니면
            else:
                linkedlist[before][2] = after
                linkedlist[after][0] = before
                nowidx = after

        elif c[0] == 'Z':
            now = stack.pop()
            before = linkedlist[now][0]
            after = linkedlist[now][2]
            OX[now] = 'O'
            if before != -1:
                linkedlist[before][2] = now
            if after != -1:
                linkedlist[after][0] = now

    # linkedlist를 list로 복귀

    return ''.join(OX)


print(solution(
    8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
))