from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    baduser = defaultdict(int)
    goodtobad = defaultdict(list)
    gooduser = defaultdict(int)

    report = list(set(report))
    # 신고 횟수 카운트
    for r in report:
        good, bad = r.split()
        baduser[bad] += 1
        goodtobad[good].append(bad)

    # keylist 넘는데 value 있으면 카운트
    for key, value in baduser.items():
        if value>=k:
            for g in goodtobad.keys():
                if key in goodtobad[g]:
                    gooduser[g] += 1

    for p in id_list:
        answer.append(gooduser[p])

    return answer

print(solution(
["muzi", "frodo", "apeach", "neo"],
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
2))