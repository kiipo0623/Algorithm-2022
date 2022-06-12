from itertools import combinations

N = int(input())
count = -1

for i in range(1, 11):
    cand = list(map(list, combinations(range(0, 10), i)))
    update = []
    for c in cand:
        update.append(''.join(map(str, sorted(c, reverse = True))))
    update.sort()

    for u in update:
        count += 1
        if count == N:
            print(u)
            exit()

print(-1)