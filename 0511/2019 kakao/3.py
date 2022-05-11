from itertools import combinations

def solution(relation):
    COL = len(relation[0])
    ROW = len(relation)
    column = [i for i in range(COL)]
    candidate_key = []

    for idx, col in enumerate(list(map(list, zip(*relation)))):
        print(len(set(col)))
        if len(set(col)) == ROW:
            candidate_key.append({idx})

    for i in range(2, COL+1):
        for combination in list(map(set, combinations(column, i))):
            flag = True
            for candidate in candidate_key: # 최소성 확인
                if len(combination.union(candidate)) == i:
                    flag = False
                    break

            if not flag:
                continue

            # 유일성 확인
            all_relation = set()
            for rel in relation:
                tmp = []
                for attr in combination:
                    tmp.append(rel[attr])
                all_relation.add(tuple(tmp))
            if len(all_relation) == ROW:
                candidate_key.append(combination)


    return len(candidate_key)

print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))