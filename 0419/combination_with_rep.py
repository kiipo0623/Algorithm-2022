def combination(arr, r):
    # 1.
    arr = list(set(arr))
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return

        # 3.
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and(nxt == 0 or arr[nxt-1] != arr[nxt] or used[nxt-1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                used[nxt] = 0
                chosen.pop()

    generate([])

combination('AAABCD', 2)