from itertools import combinations
def minimal(cand, answer):
    print()
    for keyset in answer:
        print(keyset)
        cnt = 0
        for col in keyset:
            if col in cand:
                cnt += 1
        if cnt == len(keyset):
            return False
    return True

def uniq(cand, relation):
    global R
    result = []
    for rel in relation:
        tmp = []
        for col in cand:
            tmp.append(rel[col])
        if tuple(tmp) in result:
            return False
        result.append(tuple(tmp))
    return True

def solution(relation):
    global R
    answer = []
    R, C = len(relation), len(relation[0])
    print(R, C)
    for i in range(1, C+1):
        candidate = list(combinations([i for i in range(C)], i))
        for cand in candidate:
            if minimal(cand, answer) and uniq(cand, relation):
                answer.append(tuple(cand))

    print(answer)
    return len(answer)

print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))