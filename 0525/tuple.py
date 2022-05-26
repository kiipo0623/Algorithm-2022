import re
def solution(s):
    answer = []
    cut = s.split('},{')
    tmp = []

    for item in cut:
        item = item.split(',')
        item[0] = re.sub(r'[^0-9]','', item[0])
        item[-1] = re.sub(r'[^0-9]','', item[-1])
        tmp.append((len(item),item))

    tmp.sort()
    print(tmp)
    before = []
    for idx, val in enumerate(tmp):
        for i in range(len(val[1])):
            if val[1][i] not in before:
                answer.append(int(val[1][i]))
                break

        before = val[1]

    return answer

print(solution(
"{{1,2,3},{2,1},{1,2,4,3},{2}}"
))