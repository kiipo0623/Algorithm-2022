from itertools import combinations

def check_uniq(keys):
    global Relation, Nrow, Ncol
    data = set()

    for row in range(Nrow):
        tmp = ''
        for col in range(Ncol):
            if col in keys:
                tmp += Relation[row][col]
        data.add(tmp)
    if len(data) == Nrow:
        return True
    return False


def check_mini(key):
    global Pkey
    for sel_key in Pkey:
        L = len(sel_key)
        count = 0
        for col in sel_key:
            if col in key:
                count += 1
        if count == L:
            return False
    return True


def solution(relation):
    global Relation, Nrow, Ncol, Pkey
    Relation = relation
    Pkey = []
    Nrow, Ncol = len(relation), len(relation[0])
    columns = []
    candidates = []
    for col in range(Ncol):
        if check_uniq([col]):
            Pkey.append([col])
        else:
            columns.append(col)

    for i in range(2, len(columns) + 1):
        candidates.extend(list(map(list, combinations(columns, i))))

    for cand in candidates:
        if check_mini(cand) and check_uniq(cand):
            Pkey.append(cand)

    return len(Pkey)