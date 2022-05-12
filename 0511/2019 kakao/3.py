from itertools import combinations

def solution(relation):
    COL = len(relation[0])
    ROW = len(relation)
    candidate_key = []

    for idx, col in enumerate(list(map(list, zip(*relation)))):
        if len(set(col)) == ROW:
            candidate_key.append({idx})

    for i in range(2, COL+1):
        for combination in list(map(set, combinations(range(COL), i))):
            flag = True
            for candidate in candidate_key: # 최소성 확인
                if len(combination.union(candidate)) == i:
                    flag = False
                    break

            if not flag: # False 면 최소가 아
                continue

            # 유일성 확인
            all_relation = set()
            for rel in relation:
                tmp = ''
                for attr in combination:
                    tmp+=rel[attr]
                all_relation.add(tmp)
            if len(all_relation) == ROW:
                candidate_key.append(combination)


    return len(candidate_key)

print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))