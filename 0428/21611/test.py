def boom(line):
    global grade
    stop = False
    while not stop:
        stop = True
        leng = len(line)

        for i in range(leng-1):
            if line[i] == 0:
                continue

            if line[i] == line[i+1]:
                start, end, num, cnt = i, i+1, line[i], 1

                for j in range(i+1, leng):
                    if line[j] == num:
                        end = j
                        cnt += 1
                    else:
                        break

                if cnt>=4:
                    for idx in range(start, end+1):
                        line[idx] = 0
                    grade[num] += cnt
                    stop = False

        while 0 in line:
            line.remove(0)
    return line

grade = {1:0, 2:0, 3:0}
line = [1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 2, 1, 3, 3, 1, 1, 1, 3, 3, 3, 2, 2, 2, 1, 1, 1, 3, 3, 3, 3, 1, 2, 3, 1]
print(boom(line))