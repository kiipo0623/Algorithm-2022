from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    length = [0]*11
    for o in orders:
        length[len(o)] += 1

    for c in course:
        food_dict = defaultdict(int)
        # 조건 넘는 경우
        if sum(length[c:]) < 2:
            break

        for order in orders:
            order = sorted(order)
            combi = list(map(list, combinations(order, c)))
            for com in combi:
                com = ''.join(com)
                food_dict[com] += 1

        if max(food_dict.values()) < 2:
            continue

        for food in food_dict:
            if food_dict[food] == max(food_dict.values()):
                answer.append(food)

    answer.sort()

    return answer

print(solution(
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]
))