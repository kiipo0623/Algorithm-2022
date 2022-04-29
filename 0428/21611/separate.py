from collections import deque
def separate(line):
    line = deque(line)
    newline = []
    cnt = 1
    number = line.popleft()
    while line:
        now = line.popleft()
        if number == now: # 이전이랑 같으면
            cnt += 1
        else: # 이전이랑 다르면
            newline.append(cnt)
            newline.append(number)
            number = now
            cnt = 1
    newline.append(cnt)
    newline.append(number)

    return newline

line = [1, 1, 2, 3, 2, 3, 1, 2, 3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 2, 3, 2, 2, 1]
print(separate(line))

