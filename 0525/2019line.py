from collections import deque
def solution(C, B):
    answer = int(1e9)
    CONY = [C]
    pos, mv = C, 0
    while pos <= 200000:
        mv += 1
        pos += mv
        CONY.append(pos)

    q = deque()
    q.append((0, B))

    while q:
        time, Bpos = q.popleft()
        if Bpos<0 or Bpos>200000:
            continue
        if Bpos == CONY[time]:
            answer = min(answer, time)
            return answer
        q.append((time+1, Bpos+1))
        q.append((time+1, Bpos-1))
        q.append((time+1, Bpos*2))

    return -1

print(solution(11, 2))
print(solution(11, 1))
print(solution(6, 3))
