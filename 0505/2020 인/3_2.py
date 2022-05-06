from copy import deepcopy
def solution(gems):
    minlen, minidx = int(1e9), [-1, -1]
    kind = set(gems)
    K = len(kind)
    checker = dict()

    for item in kind:
        checker[item] = 0

    start, end = 0, 0
    c = deepcopy(checker)

    # 하나씩 체크해서 시간 단축해야 하는건지 ?
    while start<=end:
        if minlen == K-1: #이미 최선을 구했는 경우
            break

        if end == len(gems): # 끝까지 탐색한 경우
            break

        c[gems[end]] += 1

        if all(c.values()) > 0:# 성공한 경우
            while start<=end and c[gems[start]]-1 > 0 : # 더 갈수 있으면
                c[gems[start]] -= 1
                start += 1

            if end-start < minlen:
                minlen = end-start
                minidx = [start, end]

            c[gems[start]] -= 1
            start += 1
            end += 1

        else:
            end += 1

    minidx[0], minidx[1] = minidx[0]+1, minidx[1]+1
    # 마지막에 1씩 뺴주기
    return minidx

print(solution(
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
))
# print(solution(
# ["AA", "AB", "AC", "AA", "AC"]
# ))
# print(solution(
# ["XYZ", "XYZ", "XYZ"]
# ))
# print(solution(
# ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
# ))