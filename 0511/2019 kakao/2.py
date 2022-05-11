def solution(N, stages):
    answer = []
    notclear = [0] * (N + 2)
    failrate = [0] * (N + 1)

    for s in stages:
        notclear[s] += 1

    for i in range(1, N+1):
        if notclear[i] == 0:
            failrate[i] = 0
        else:
            failrate[i] = notclear[i] / sum(notclear[i:])

    failrate[0] = -1
    print(failrate)

    for _ in range(N):
        maxidx = failrate.index(max(failrate))
        answer.append(maxidx)
        failrate[maxidx] = -1

    return answer

print(solution(
    5, [2, 1, 2, 6, 2, 4, 3, 3]
    # 4, [4,4,4,4,4]
))