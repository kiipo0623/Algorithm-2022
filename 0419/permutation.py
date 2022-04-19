def permutation(arr, r):
    # 1.
    arr = sorted(arr) # 출력 이쁘게 하려고
    used = [0 for _ in range(len(arr))] # i번째 값을 썼는지
    sol = []

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            sol.append(chosen[:])
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return sol

print(permutation('ABCDE', 3))
print(permutation([1,2,3,4,5], 3))