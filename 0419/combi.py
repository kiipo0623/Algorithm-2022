def combination(arr, r):
    # 1.
    arr = sorted(arr)
    sol = []

    # 2.
    def generate(chosen):
        if len(chosen) == r:
            sol.append(chosen[:])
            return

        # 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()

    generate([])
    return sol

print(combination('ABCDE', 3))
