from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    exp = []
    tmp = ''

    for i in range(len(expression)):
        if expression[i] not in ['*', '-', '+']:
            tmp += expression[i]
        else:
            exp.append(tmp)
            exp.append(expression[i])
            tmp = ''
    exp.append(tmp)

    order = list(permutations(['*', '+', '-']))
    print(exp)


    for o in order:
        queuebefore, queueafter = deque(exp), deque()
        for ari in o:
            while queuebefore:
                now = queuebefore.popleft()
                if now != ari:
                    queueafter.append(now)
                else:
                    bf = queueafter.pop()
                    af = queuebefore.popleft()
                    res = eval(bf+now+af)
                    queueafter.append(str(res))
            queuebefore, queueafter = queueafter, queuebefore
        answer = max(answer, abs(int(queuebefore[0])))

    return answer

print(solution(
"100-200*300-500+20"
))