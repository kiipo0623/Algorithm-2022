from collections import defaultdict
def cut(strname, dictname):
    global dict1, dict2
    for i in range(len(strname)-1):
        tmp = strname[i:i+2]
        if not tmp.isalpha():
            continue
        dictname[tmp.lower()] += 1


def solution(str1, str2):
    global dict1, dict2
    dict1, dict2 = defaultdict(int), defaultdict(int)
    cut(str1, dict1)
    cut(str2, dict2)

    uni = set(dict1.keys()).union(set(dict2.keys()))
    mom, son = 0, 0

    # print(dict1)
    # print(dict2)
    # print(uni)

    for item in uni:
        son += min(dict1[item], dict2[item])
        mom += max(dict1[item], dict2[item])

    for item in dict1.keys():
        if item not in uni:
            mom += 1
    for item in dict2.keys():
        if item not in uni:
            mom += 1


    return int((son/mom)*65536)

print(solution(
    'FRANCE', 'french'
))