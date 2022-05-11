from itertools import permutations

weaks = []
def make_weaks(n, weak):
    cnt = 1
    weaks.append(weak)
    while cnt != len(weak):
        tmp = []
        for i in range(cnt, len(weak)):
            tmp.append(weak[i])
        for i in range(cnt):
            tmp.append(weak[i]+n)




def solution(n, weak, dist):
    make_weaks(n, weak)