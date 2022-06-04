Relation = []
def checkuniq(itemlist):
    global Relation
    tuplelist = []
    for rel in Relation:
        tmp = []
        for item in itemlist:
            tmp.append(rel[item])

        if tuple(tmp) in tuplelist:
            return False
        tuplelist.append(tuple(tmp))
    return True

def checkmini(itemlist):
    global answer
    for ans in answer:
        cnt = 0
        for a in ans:
            if a in itemlist:
                cnt += 1
        if cnt == len(ans):
            return False
    return True

# 이렇게 했을 때 더 큰 게 먼저들어가면 유일성을 만족하지 않나 ???? 123이 먼저들어가는경우
# 해결하기 위해서는 그냥 개수 순서대로 하는수밖에없음
def bt(itemlist):
    global answer, C
    print("itemlist", itemlist)
    if checkuniq(itemlist) and checkmini(itemlist):
        answer.append(tuple(itemlist))
        return

    for idx in range(C):
        if idx not in itemlist:
            itemlist.append(idx)
            bt(itemlist)
            itemlist.pop()


def solution(relation):
    global Relation, answer, R, C
    Relation = [a[:] for a in relation]
    answer = []
    R, C = len(relation), len(relation[0])
    for i in range(C):
        bt([i])
    return len(answer)

print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))