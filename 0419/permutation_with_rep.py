def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    sol = []

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            sol.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)
    return sol

print(permutation('AABC', 2))