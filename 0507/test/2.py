from collections import deque
def simul(visit):
    L = len(visit)
    TF = list(visit.values())
    queue1 = deque(TF[:L//2])
    queue2 = deque(TF[L//2:])
    count = 0
    while queue1:
        now = queue1.popleft()
        queue2.append(now)
        count += 1
        if len(set(queue1)) == 1:
            break

    while queue2:
        now = queue2.popleft()
        queue1.append(now)
        count += 1
        if len(set(queue2)) == 1:
            break

    if len(set(queue1)) == 1 and len(set(queue2)) == 1:
        return count
    else:
        return -1

queue1 = [3,2,7,2]
queue2 = [4,6,5,1]
visit1 = {0: False, 1: True, 2: True, 3: True, 4: True, 5: False, 6: False, 7: False}
visit2 = {0: False, 1: True, 2: True, 3: False, 4: False, 5: True, 6: False, 7: False}

print(simul(visit1))
print(simul(visit2))