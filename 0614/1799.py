def backtrack(idx, cnt, selected):
    global answer
    if idx == place_cnt:
        answer = max(answer, cnt)
        return

    r, c = place_cand[idx]

    flag = True
    for i in range(1, N):
        for s in selected:
            if (r-i, c-i) == s or (r+i, c+i) == s or (r-i, c+i) == s or (r+i, c-i) == s:
                flag = False
                break
        if not flag:
            break

    if flag:
        selected.append((r, c))
        backtrack(idx+1, cnt+1, selected)
        selected.pop()

    # 해당 위치에 안놓는 경우는 무조건 가능
    backtrack(idx+1, cnt, selected)


N = int(input())
place_cand = []
place_cnt = 0
answer = 0
for i in range(N):
    tmp = list(map(str, input().split()))
    for j in range(N):
        if tmp[j] == '1':
            place_cnt += 1
            place_cand.append((i, j))

backtrack(0, 0, [])
print(answer)

