# 시험장 나누기
from itertools import combinations
dp_sum = [0] * 10000

def find_sum(idx, num, links):
    left, right = links[idx]
    if left == -1 and right == -1:
        dp_sum[idx] = num[idx]
    elif left == -1:
        dp_sum[idx] = find_sum(right, num, links) + num[idx]
    elif right == -1:
        dp_sum[idx] = find_sum(left, num, links) + num[idx]
    else:
        dp_sum[idx] = find_sum(left,num,  links) + find_sum(right, num, links) + num[idx]
    return dp_sum[idx]

def solution(k, num, links):
    N = len(num)
    answer = 0
    tree = dict()
    for idx, link in enumerate(links):
        for l in link:
            if l != -1:
                tree[l] = idx

        if dp_sum[idx] == 0:
            find_sum(idx, num, links)
        else:
            continue

    root = dp_sum.index(max(dp_sum))
    print(tree)
    combination = list(combinations(range(N), k))

    for combi in combination:
        res = []
        dp = dp_sum[:]
        for node in combi:
            res.append(dp[node])







    return answer

print(solution(
    3, [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1], [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
))