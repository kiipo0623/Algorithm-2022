from collections import deque
from copy import deepcopy

def simulate():
    global A, robot
    cnt = 1
    while True:
        out = 0
        # 벨트 회전
        tmp = A.pop()
        A.appendleft(tmp)
        listA = list(A)
        reverseA = list(reversed(listA[N:]))
        A = deque(listA[:N]+reverseA)

        # 로봇 회전
        robot.pop()
        robot.appendleft(False)

        # i=1부터 로봇 이동
        new_robot = [False]*N
        for i in range(0, N-1):
            if robot[i+1]==False and A[i+1] > 0:
                new_robot[i+1] = True
                A[i+1] -= 1

        # 로봇 올리기
        if A[0] > 0:
            new_robot[0] = True

        for i in range(N):
            if A[i] == 0:
                out += 1

        if i>=K:
            return cnt

        cnt += 1
        robot = deepcopy(deque(new_robot))

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = deque(A)
robot = [False]*N
robot = deque(robot)
print(simulate())