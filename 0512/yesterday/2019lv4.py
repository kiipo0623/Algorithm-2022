from collections import Counter
def solution(food_times, k):
    before_eat = 0
    already_eat = 0
    people_num = len(food_times)
    people_count = Counter(food_times)
    rmv_list = sorted(people_count)
    rmv_idx = 0

    while True:
        if len(rmv_list) <= rmv_idx:
            return -1

        already_eat += (rmv_list[rmv_idx]-before_eat)*people_num

        if already_eat > k: # 똑같을 경우
            already_eat -= (rmv_list[rmv_idx]-before_eat)*people_num
            rmv_idx -= 1
            break

        before_eat = rmv_list[rmv_idx]
        people_num -= people_count[rmv_list[rmv_idx]]
        rmv_idx += 1

    leave_food = []
    k -= already_eat

    for idx, food in enumerate(food_times):
        if food > rmv_list[rmv_idx]:
            leave_food.append(idx+1)

    if len(leave_food) == 0:
        return -1
    else:
        return leave_food[k%len(leave_food)]

print(solution(
    [2, 2, 2, 2, 2], 9
))