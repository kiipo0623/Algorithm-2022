from itertools import combinations
from collections import deque
def go_for_lunch(people, stairs):
    # 계단까지 도착하는 시간
    s = []

    for person in people:
        s.append(abs(person[0]-stairs[0])+abs(person[1]-stairs[1]))

    s = deque(sorted(s))

    e = deque()

    time = 0
    curr = 0 # 현재 계단에 있는 사람 수

    while s:
        time += 1

        # 이동을 완료했을 경우
        while e and e[0] == time:
            e.popleft()
            curr -= 1

        while s[0] < time:
            # 계단 이동
            if curr < 3:
                s.popleft()
                if not s:
                    time += grid[stairs[0]][stairs[1]]
                    break

                e.append(time+grid[stairs[0]][stairs[1]])
                curr += 1
            else:
                break
    return time

T = int(input())

for t in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                people.append((i, j))
            elif grid[i][j] >= 2:
                stairs.append((i, j))

    total = float('inf')
    for n in range(N):
        for people1 in combinations(people, n):
            people2 = list(set(people) - set(people1))
            time = max(go_for_lunch(people1, stairs[0]), go_for_lunch(people2, stairs[1]))
            total = min(total, time)
    print(total)