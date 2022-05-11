def solution(food_times, k):
    answer = 0
    sorted_food_times = sorted(food_times)

    n_remain_foods = len(food_times)
    accumulated_time = 0 # 한번에 이만큼 제거
    jump_time = 0
    period_time = 0 # 이전에 깎은 시간

    # 나의 궁금증 : 작은 시간이 겹치면?
    for time in sorted_food_times:
        jump_time = time - period_time # 이번에 점프할 시간
        accumulated_time += jump_time * n_remain_foods # 이번턴에서 스킵되는 시간

        if k < accumulated_time:
            accumulated_time -= jump_time * n_remain_foods
            break

        period_time = time
        n_remain_foods -= 1

    if n_remain_foods == 0:
        return -1

    k -= accumulated_time
    remain_iteration = k%n_remain_foods

    li = []
    for idx, value in enumerate(food_times):
        if value > period_time:
            li.append(idx+1)

    answer = li[remain_iteration]

    return answer
