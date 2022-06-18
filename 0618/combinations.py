comb_sol = []
perm_sol = []
def combination(data, idx, selected, target, N):
    global comb_sol
    if len(selected) == target:
        comb_sol.append(selected[:])
        return

    for i in range(idx, N):
        selected.append(data[i])
        combination(data, i+1, selected, target, N)
        selected.pop()


def permutation(data, idx, selected, visited, target, N):
    global perm_sol
    if len(selected) == target:
        perm_sol.append(selected[:])
        return

    for i in range(N):
        if visited[i]:
            continue
        selected.append(data[i])
        visited[i] = True
        permutation(data, idx+1, selected, visited, target, N)
        visited[i] = False
        selected.pop()



testdata = ['A', 'B', 'C', 'D', 'E', 'F']
combination(testdata, 0, [], 3, len(testdata))
permutation(testdata, 0, [], [False]*len(testdata), 3, len(testdata))
# print(comb_sol)
# print(len(comb_sol))
print(perm_sol)
print(len(perm_sol))