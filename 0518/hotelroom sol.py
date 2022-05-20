from collections import deque
def solution(k, room_number):
    answer = []
    save = {}
    q = deque()
    for room in room_number:
        while save.get(room):
            q.append(room)
            room = save[room]
        q.append(room)
        answer.append(room)

        while q:
            tmp = q.popleft()
            save[tmp] = room+1
    return answer

print(solution(
    10, [1,3,4,1,3,1]
))
# 빈 방 : 즉시 부여
# 빈 방X : 부모 노드 방문 (반복) > 방문한 모든 노드에게 배정 방 번호+1 갱신

