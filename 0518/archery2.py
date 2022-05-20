# 완전탐색
from itertools import combinations_with_replacement
from collections import Counter

def getgrade(apeach, ryan):
    a, r = 0, 0
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue
        elif apeach[i] >= ryan[i]:
            a+= (10-i)
        elif apeach[i] < ryan[i]:
            r += (10-i)
    if a >= r: # 졌을 떄
        return -1
    else: # 이겼을 때 : 차이가 가장 크도록
        return (r-a)

def solution(n, info):
    answer = [-1]
    bestchoice, bestdis = [0]*11, -1
    # 카운터 값 = idx
    combination = list(combinations_with_replacement(range(0, 11), n))
    for combi in combination:
        ryan = [0]*11
        for key, value in Counter(combi).items():
            ryan[key] = value
            nowgrade = getgrade(info, ryan)

            if nowgrade == -1: # 졌음
                continue
            else: # 이겼음
                if bestdis < nowgrade: # 이번 차이가 더 큼
                    bestchoice, bestdis = ryan[:], nowgrade
                elif bestdis == nowgrade: # 차이가 똑같다
                    for i in range(10, -1, -1):
                        if bestchoice[i] > ryan[i]:
                            break
                        elif bestchoice[i] < ryan[i]:
                            bestchoice = ryan[:]
                            break

    if bestchoice != [0]*11:
        return bestchoice
    else:
        return answer

print(solution(
    # 5, [2,1,1,1,0,0,0,0,0,0,0]
    # 1, [1,0,0,0,0,0,0,0,0,0,0]
    9, [0,0,1,2,0,1,1,1,1,1,1]
))