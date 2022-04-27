def combination(lst, N):
    candidate = []

    def generate(select, cnt):
        if cnt == N//2:
            candidate.append(select[:])
            return

        start = lst.index(select[-1]) + 1 if select else 0
        for i in range(start, N):
            select.append(lst[i])
            generate(select, cnt + 1)
            select.pop()

    generate([], 0)
    return candidate

lst = [1,2,3,4,5,6]
N = 6
print(combination(lst, N))

