def solution(relation):
    answer_list = []
    for i in range(1, 1<<len(relation[0])): # 전부 선택할 때까지
        tmp_set = set()
        for j in range(len(relation)): # Relation
            tmp = ''
            for k in range(len(relation[0])): # Attribute
                if i & ( 1<< k): # k번째가 선택되어 있으면
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)
        print(tmp_set)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num: # 다 포함되어 있으면
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)

    return len(answer_list)


print(solution(
[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
))