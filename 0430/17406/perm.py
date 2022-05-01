def permutation(cnt, select, visit):
    if cnt == K:
        print(select)

    for i in range(K):
        if visit[i] == False:
            select.append(lst[i])
            visit[i] = True
            permutation(cnt + 1, select, visit)
            select.pop()
            visit[i] = False

K = 3
lst = [i for i in range(K)]
permutation(0, [], [False]*K)
