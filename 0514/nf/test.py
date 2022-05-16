def solution(recruits, s1, s2):
    candidate = [0, 0]

    MAX_SUM = 0
    for e1 in range(0, 101):
        for e2 in range(0, 101):
            j, s, e = 0, 0, 0
            for idx, recruit in enumerate(recruits):
                if recruit[0] >= e1 and recruit[1] >= e2:
                    e += 1
                elif recruit[0] >= s1 or recruit[1] >= s2:
                    s += 1
                else:
                    j += 1

            print(e1, e2)
            print("e", e)
            print("s", s)
            print("j", j)
            print()
            if 0 < e < s < j and e1 + e2 >= MAX_SUM:

                if e1 + e2 > MAX_SUM:
                    MAX_SUM = e1 + e2
                    candidate[0], candidate[1] = e1, e2
                elif e1 + e2 == MAX_SUM:
                    if candidate[0] > e1:
                        continue
                    else:
                        candidate[0], candidate[1] = e1, e2
    return candidate

print(solution(
[[1, 50], [1, 60], [3, 70], [0, 65], [2, 50], [1, 90]], 2, 70
))