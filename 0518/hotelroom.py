def solution(k, room_number):
    answer = []
    save = dict()

    for room in room_number:
        if not save.get(room): # 그냥 거기 넣을 수 있었음
            answer.append(room)
            if not save.get(room+1):
                save[room] = room+1
            else:
                save[room] = save[room+1]

        else: #비어있지 않았음
            answer.append(save[room])
            save[room] = save[room+1] # 여기서 갱신해줘야하는데
    return answer

print(solution(
    10, [1,3,4,1,3,1]
))