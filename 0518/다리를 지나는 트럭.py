from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    bridge = deque(bridge)
    left_weight, left_truck = weight, deque(truck_weights)
    cnt = 0

    while True:
        answer += 1
        # 트럭 하나 나오고
        now = bridge.popleft()
        left_weight += now
        if now != 0:
            cnt += 1
        if cnt == len(truck_weights): break
        # 트럭 하나 들어가고
        if left_truck and left_weight >= left_truck[0]:
            left_weight -= left_truck[0]
            bridge.append(left_truck.popleft())
        else:
            bridge.append(0)

    return answer

print(solution(
100, 100, [10]*10
))
