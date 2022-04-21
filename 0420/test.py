def combination(maxdepth, chosen):
    global sol_combi
    if len(chosen) == maxdepth:
        sol_combi.append(chosen[:])
        return

    start = array.index(chosen[-1]) + 1 if chosen else 0
    for i in range(start, len(array)):
        chosen.append(array[i])
        combination(maxdepth, chosen)
        chosen.pop()

def permutation(maxdepth, chosen, used):
    global sol_permu
    if len(chosen) == maxdepth:
        sol_permu.append(chosen[:])
        return

    for i in range(len(array)):
        if not used[i]:
            chosen.append(array[i])
            used[i] = 1
            permutation(maxdepth, chosen, used)
            chosen.pop()
            used[i] = 0


array = [1,2,3,4,5,6]
sol_combi, sol_permu = [], []
combination(2, [])
permutation(2, [], [0 for _ in range(len(array))])
print(sol_combi)
print(sol_permu)
print(len(sol_combi), len(sol_permu))
