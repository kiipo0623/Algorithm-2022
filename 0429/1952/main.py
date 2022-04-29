def bt(now, cost, checker):
    global answer
    if all(checker) == True:
        answer = min(answer, cost)

    # 1일권
    checker[now+1] = True
    bt(now+1, cost + plan[now+1]*money[0], checker)
    checker[now+1] = False

    # 1달권
    checker[now+1] = True
    bt(now+1, cost + money[1])
    checker[now+1] = False

    # 3달권
    for i in range(1, 4):
        if now+i<=13:
            checker[now+i] = True
    bt(now+3, cost + money[2])
    for i in range(1, 4):
        if now + i <= 13:
            checker[now+i] = False

    # 1년권
    for i in range(1, 12):
        if now + i <= 13:
            checker[now+i] = True
    bt(now+12, cost + money[3])
    for i in range(1, 12):
        if now + i <= 13:
            checker[now+i] = False


T = int(input())
for t in range(1, T+1):
    money = list(map(int, input().split())) # 1일 1달 3달 1년
    plan = [0] + list(map(int, input().split()))
    answer = int(1e9)
    checker = [False]*13
    checker[0] = True
    bt(0, 0, checker)
    print(answer)