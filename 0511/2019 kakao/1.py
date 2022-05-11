from collections import defaultdict, deque


def solution(record):
    answer = []
    idname = defaultdict(str)
    inout = deque()

    for r in record:
        if r[:5] == "Leave":
            _, id = r.split()
            inout.append(("Leave", id))
        else:
            first, second, third = r.split()
            if first == "Enter":
                inout.append((first, second))
                idname[second] = third
            elif first == "Change":
                idname[second] = third

    while inout:
        todo, id = inout.popleft()
        if todo == "Enter":
            answer.append(idname[id]+"님이 들어왔습니다")
        elif todo == "Leave":
            answer.append(idname[id]+"님이 나갔습니다.")

    return answer

print(solution(
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
))