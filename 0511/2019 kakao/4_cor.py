def solution(food_times, k):
    idx = 0
    N = len(food_times)

    def find_food_index(idx):
        while True:
            if food_times[idx] > 0:
                return idx
            else:
                idx = (idx + 1) % N

    print(food_times)
    for _ in range(k):
        nowidx = find_food_index(idx)
        food_times[nowidx] -= 1
        idx = (nowidx+1)%N
        if sum(food_times) == 0:
            return -1

    return find_food_index(idx) + 1

print(solution(
    [3,1,2], 5
))