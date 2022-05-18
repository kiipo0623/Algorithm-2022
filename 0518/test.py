from itertools import *

def cmp(a, b):
    return a[::-1] > b[::-1]

def solution(n, info):
    ret = [-1]*12
    for comb in combinations_with_replacement(range(11), n):
        arrow = [0]*12
        score = 0
        for x in comb:
            arrow[x] += 1
        for i in range(11):
            if arrow[i] > info[i]:
                score += (10 - i)
            elif info[i] != 0:
                score -= (10 - i)
        if score <= 0:
            continue
        arrow[11] = score
        if cmp(arrow, ret):
            ret = arrow[:]
    if ret[0] == -1:
        return [-1]
    return ret[:-1]