N = int(input())
count = -1

def bt(limit, now):
    global N, count
    if len(now) == limit:
        count += 1
        if count == N:
            print(now)
            exit()
        return

    # 아예 처음부터 만들어야 하는 경우
    if len(now) == 0:
        for i in range(limit-1, 10):
            now += str(i)
            bt(limit, now)
            now = ''

    else:
        for i in range(int(now[-1])):
            if limit - len(now) - 1 > i:
                continue
            now += str(i)
            bt(limit, now)
            now = now[:-1]

for i in range(1, 11):
    bt(i, '')
print(-1)