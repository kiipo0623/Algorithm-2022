from collections import deque

def simulate():
    cnt = 1
    global A, robot

    while True:
        # 벨트 회전
        tmp = A.pop()
        A.appendleft(tmp)

        # 로봇 회전
        robot.pop()
        robot.appendleft(False)

        # 로봇 이동
        robotlist = list(robot)
        Alist = list(A)
        robotlist[-1] = False
        for i in range(N-2, -1, -1):
            if robotlist[i] == True and robotlist[i+1] == False and Alist[i+1]>0:
                robotlist[i+1] = True
                robotlist[i] = False
                Alist[i+1] -= 1

        # 새 로봇
        if Alist[0] > 0:
            Alist[0] -= 1
            robotlist[0] = True
        # 카운트

        if Alist.count(0) >= K:
            return cnt


        # 후처리
        cnt += 1
        A = deque(Alist)
        robot = deque(robotlist)


N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
robot = deque([False]*N)

print(simulate())