from collections import defaultdict
def solution(stones, k):
    answer = 0
    val_idx = defaultdict(list)
    numset = set()

    for idx, val in enumerate(stones):
        val_idx[val].append(val)
        numset.add(val)

    numset = sorted(list(numset))

    for num in numset:
        cnt = 0
        for stoneidx in val_idx[num]:
            for i in range(stoneidx, stoneidx+k):
                if stones[i] <= num:
                    cnt += 1


    return answer