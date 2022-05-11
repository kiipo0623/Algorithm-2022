# 호텔 방 배정
def solution(k, room_number):
    answer = []
    ava = {i:False for i in range(1, k+1)}

    for room in room_number:
        if not ava[room]:
            ava[room] = True
            answer.append(room)

        else:
            while ava[room]:
                room += 1
            ava[room] = True
            answer.append(room)

    return answer

print(solution(
    10, [1,3,4,1,3,1]
))